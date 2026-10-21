import { Marked } from 'marked';
import markedKatex from 'marked-katex-extension';
import { withBase } from './base';

export interface TocItem {
  id: string;
  text: string;
  level: number;
}

export interface ParsedMarkdown {
  html: string;
  toc: TocItem[];
}

export function parseMarkdown(rawContent: string, currentSeasonSlug: string = 'season-01'): ParsedMarkdown {
  const toc: TocItem[] = [];

  // Strip initial chapter header lines that are displayed in the UI header
  // (e.g. # Chapter X..., **Series:** ..., **Sequential Context:** ..., ---)
  let cleanContent = rawContent;
  const headerEndIndex = rawContent.indexOf('\n---\n');
  if (headerEndIndex !== -1 && headerEndIndex < 1000) {
    cleanContent = rawContent.substring(headerEndIndex + 5).trim();
  }

  const marked = new Marked();

  // KaTeX math rendering
  marked.use(
    markedKatex({
      throwOnError: false,
    })
  );

  // Custom renderer for links and headings
  marked.use({
    renderer: {
      heading({ text, depth }) {
        // Create slug ID
        const rawText = text.replace(/<[^>]*>/g, '').trim();
        const id = rawText
          .toLowerCase()
          .replace(/[^\w\s-]/g, '')
          .replace(/\s+/g, '-');

        if (depth === 2 || depth === 3) {
          toc.push({
            id,
            text: rawText,
            level: depth,
          });
        }

        return `<h${depth} id="${id}" class="content-heading heading-l${depth}"><a href="#${id}" class="heading-anchor" aria-hidden="true">#</a><span>${text}</span></h${depth}>`;
      },

      link({ href, title, text }) {
        if (!href) return text;

        let targetHref = href;
        let isExternal = false;

        if (href.startsWith('http://') || href.startsWith('https://')) {
          isExternal = true;
        } else {
          // Resolve relative markdown links
          let [url, hash] = href.split('#');
          const anchor = hash ? `#${hash}` : '';

          if (url.includes('timeline.md')) {
            targetHref = withBase(`/timeline${anchor}`);
          } else if (url.includes('guide.md')) {
            targetHref = withBase(`/guide${anchor}`);
          } else if (url.includes('continuity.md')) {
            targetHref = withBase(`/continuity${anchor}`);
          } else if (url.endsWith('README.md')) {
            if (url.includes('season-')) {
              const sMatch = url.match(/season-0?(\d)/);
              if (sMatch) {
                targetHref = withBase(`/seasons/season-0${sMatch[1]}${anchor}`);
              } else {
                targetHref = withBase(`/${anchor}`);
              }
            } else {
              targetHref = withBase(`/${anchor}`);
            }
          } else {
            const crossSeasonMatch = url.match(/season-0?(\d)\/episodes\/(ep-[a-z0-9-]+)\.md/);
            if (crossSeasonMatch) {
              const sNum = crossSeasonMatch[1].padStart(2, '0');
              targetHref = withBase(`/episodes/season-${sNum}/${crossSeasonMatch[2]}${anchor}`);
            } else {
              const epMatch = url.match(/(ep-[a-z0-9-]+)\.md/);
              if (epMatch) {
                targetHref = withBase(`/episodes/${currentSeasonSlug}/${epMatch[1]}${anchor}`);
              }
            }
          }
        }

        const titleAttr = title ? ` title="${title}"` : '';
        const extAttr = isExternal ? ' target="_blank" rel="noopener noreferrer"' : '';
        return `<a href="${targetHref}"${titleAttr}${extAttr} class="prose-link">${text}</a>`;
      },

      table({ header, rows }) {
        return `<div class="table-container"><table><thead>${header}</thead><tbody>${rows}</tbody></table></div>`;
      },

      code({ text, lang }) {
        // Detect ASCII charts or diagrams
        const isDiagram = !lang || lang === 'text' || lang === 'ascii' || text.includes('+---') || text.includes('|');
        const diagramClass = isDiagram ? 'ascii-diagram' : '';
        return `<pre class="code-block ${diagramClass}"><code class="language-${lang || 'text'}">${text}</code></pre>`;
      },

      blockquote({ text }) {
        return `<blockquote class="prose-quote">${text}</blockquote>`;
      },
    },
  });

  const html = marked.parse(cleanContent) as string;

  return {
    html,
    toc,
  };
}
