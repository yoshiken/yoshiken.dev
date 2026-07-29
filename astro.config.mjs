import { satteri } from "@astrojs/markdown-satteri";
import sitemap from "@astrojs/sitemap";
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://yoshiken.dev",
  output: "static",
  trailingSlash: "never",
  build: {
    format: "file",
  },
  markdown: {
    processor: satteri({
      features: {
        smartPunctuation: false,
      },
    }),
  },
  integrations: [
    sitemap({
      filter: (page) => page !== "https://yoshiken.dev/404.html",
    }),
  ],
});
