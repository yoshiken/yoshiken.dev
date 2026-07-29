import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const articles = (await getCollection("articles")).sort(
    (a, b) => b.data.date.getTime() - a.data.date.getTime(),
  );

  return rss({
    title: "yoshiken.dev",
    description:
      "yoshikenがプログラミングや日記、ポエムを書いていくページです。",
    site: context.site ?? "https://yoshiken.dev",
    items: articles.map((article) => ({
      title: article.data.title,
      description: article.data.summary,
      pubDate: article.data.date,
      link: new URL(`/articles/${article.id}`, context.site).toString(),
    })),
  });
}
