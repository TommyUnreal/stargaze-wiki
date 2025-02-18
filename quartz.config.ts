import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Stargaze Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "cs-CZ",
    baseUrl: "https://tommyunreal.github.io/stargaze-wiki/",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    generateSocialImages: false,
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Roboto Condensed", // Clean and modern font for headers
        body: "Roboto Condensed", // Serif font for body text, great for readability
        code: "Fira Code", // Monospaced font for code, with good readability
      },
      colors: {
        lightMode: {
          light: "#ffffff", // Pure white background for light mode
          lightgray: "#f5f5f5", // Very light gray for subtle contrasts
          gray: "#7a7a7a", // Medium gray for secondary text
          darkgray: "#4e4e4e", // Dark gray for primary text
          dark: "#2b2b2b", // Almost black for strong contrasts
          secondary: "#3a6ea5", // Muted blue for accents, like a calm sky
          tertiary: "#a53a6e", // Muted purple for tertiary elements
          highlight: "rgba(58, 110, 165, 0.1)", // Subtle blue highlight
          textHighlight: "#a53a6e88", // Subtle purple text highlight
          text_em: "#228b22", // Green color for emphasized text
          text_strong: "#333333", // Slightly darker than normal text for strong emphasis
        },
        darkMode: {
          light: "#1a1a1a", // Dark background for dark mode
          lightgray: "#2a2a2a", // Slightly lighter gray for subtle contrasts
          gray: "#7a7a7a", // Medium gray for secondary text
          darkgray: "#d4d4d4", // Light gray for primary text
          dark: "#ebebec", // Almost white for strong contrasts
          secondary: "#4fc3f7", // Soft blue for accents, like a star
          tertiary: "#ff6f00", // Muted orange for tertiary elements
          highlight: "rgba(79, 195, 247, 0.1)", // Subtle blue highlight
          textHighlight: "#ff6f0088", // Subtle orange text highlight
		  text_em: "#92bd92", // Green color for emphasized text
		  text_strong: "#cccccc", // Slightly lighter than normal text for strong emphasis
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config