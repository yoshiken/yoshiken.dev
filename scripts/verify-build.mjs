import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { basename, extname, join } from "node:path";

const articleSourceDirectory = "src/content/articles";
const articleOutputDirectory = "dist/articles";
const slugs = readdirSync(articleSourceDirectory)
  .filter((file) => extname(file) === ".md")
  .map((file) => basename(file, ".md"))
  .sort();
const outputSlugs = readdirSync(articleOutputDirectory)
  .filter((file) => extname(file) === ".html")
  .map((file) => basename(file, ".html"))
  .sort();

assert.deepEqual(outputSlugs, slugs, "Every article must generate one HTML file.");

for (const file of [
  "dist/index.html",
  "dist/about.html",
  "dist/format.html",
  "dist/404.html",
  "dist/feed.xml",
  "dist/robots.txt",
  "dist/sitemap-index.xml",
  "dist/sitemap-0.xml",
  "dist/CNAME",
  "dist/favicon.ico",
  "dist/ogp.png",
]) {
  assert.ok(existsSync(file), `${file} must be generated.`);
}

const index = readFileSync("dist/index.html", "utf8");
const feed = readFileSync("dist/feed.xml", "utf8");
const sitemap = readFileSync("dist/sitemap-0.xml", "utf8");

for (const slug of slugs) {
  const url = `https://yoshiken.dev/articles/${slug}`;
  assert.match(index, new RegExp(`href="/articles/${slug}"`));
  assert.ok(feed.includes(`<link>${url}</link>`), `${slug} must be in the feed.`);
  assert.ok(sitemap.includes(`<loc>${url}</loc>`), `${slug} must be in the sitemap.`);

  const article = readFileSync(join(articleOutputDirectory, `${slug}.html`), "utf8");
  assert.ok(
    article.includes(`<link rel="canonical" href="${url}">`),
    `${slug} must have the canonical URL.`,
  );
}

assert.ok(!index.includes("2025-09-13"), "The stale article link must not remain.");

console.log(`Verified ${slugs.length} articles and all required site outputs.`);
