export const SetOptions = {
  javaScript: "javascript",
  html: "html",
  css: "css",
} as const;

export type Set = (typeof SetOptions)[keyof typeof SetOptions];
