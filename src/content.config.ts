import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const articles = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    category: z.enum(["blog", "diary", "tech"]),
    summary: z.string(),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    category: z.union([
      z.enum(["blog", "diary", "tech"]),
      z.array(z.enum(["blog", "diary", "tech"])),
    ]),
    summary: z.string(),
  }),
});

export const collections = { articles, pages };
