#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const rootDir = path.resolve(__dirname, "..");
const destinationArg = process.argv[2];
const destinationDir = destinationArg
  ? path.resolve(process.cwd(), destinationArg)
  : process.cwd();

const includePaths = [
  "AGENTS.md",
  "CHANGELOG.md",
  "CODE_OF_CONDUCT.md",
  "CONTRIBUTING.md",
  "CONTEXT.md",
  "LICENSE",
  "README.md",
  "SKILL.md",
  "assets",
  "skills"
];

function exists(filePath) {
  try {
    fs.accessSync(filePath, fs.constants.F_OK);
    return true;
  } catch {
    return false;
  }
}

function ensureDirectory(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function copyRecursive(fromPath, toPath) {
  const stats = fs.statSync(fromPath);

  if (stats.isDirectory()) {
    ensureDirectory(toPath);
    for (const entry of fs.readdirSync(fromPath)) {
      copyRecursive(path.join(fromPath, entry), path.join(toPath, entry));
    }
    return;
  }

  ensureDirectory(path.dirname(toPath));
  fs.copyFileSync(fromPath, toPath);
}

function main() {
  ensureDirectory(destinationDir);

  const targetRoot = path.join(destinationDir, "android-engineering-skill");
  if (exists(targetRoot)) {
    console.error("[android-engineering-skill] Destination already exists:");
    console.error(`  ${targetRoot}`);
    console.error("Use another path or remove the existing folder first.");
    process.exit(1);
  }

  ensureDirectory(targetRoot);

  for (const relativePath of includePaths) {
    const sourcePath = path.join(rootDir, relativePath);
    const destinationPath = path.join(targetRoot, relativePath);
    copyRecursive(sourcePath, destinationPath);
  }

  console.log("[android-engineering-skill] Installed successfully.");
  console.log(`Location: ${targetRoot}`);
  console.log("Next step: review README.md and SKILL.md");
}

main();
