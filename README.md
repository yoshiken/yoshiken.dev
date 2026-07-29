# yoshiken.dev

[yoshiken.dev](https://yoshiken.dev/) のソースです。AstroでMarkdownから静的HTMLを生成し、GitHub Pagesで公開しています。

## 必要な環境

- Node.js 22.12以上
- pnpm 10.30.3

Corepackを有効にすると、`package.json`で指定したpnpmを利用できます。

```sh
corepack enable
pnpm install
```

## ローカル開発

```sh
pnpm dev
```

`http://localhost:4321`でプレビューできます。

```sh
pnpm check
pnpm verify
pnpm preview
```

## 記事を書く

`src/content/articles/<slug>.md`を追加します。ファイル名が`/articles/<slug>`のURLになります。

```md
---
title: "記事タイトル"
date: "2026-07-29T23:00:00+09:00"
category: "tech"
summary: "記事の概要"
---

## 見出し

本文をMarkdownで書きます。
```

`category`は`blog`、`diary`、`tech`のいずれかです。SpeakerDeck等の信頼できる埋め込みには生HTMLも利用できます。

## 公開

`main`へのpushをトリガーに、GitHub Actionsが型検査とビルドを実行し、生成した`dist/`をGitHub Pagesへデプロイします。生成済みHTMLはGit管理しません。
