#!/bin/bash

# Build macOS DMG for Claudia
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project info
PROJECT_NAME="Claudia"
OUTPUT_DIR="build/mac"

echo -e "${BLUE}🚀 Starting macOS DMG build for ${PROJECT_NAME}...${NC}"

# Check if we're in the correct directory
if [ ! -f "package.json" ] || [ ! -d "src-tauri" ]; then
    echo -e "${RED}❌ Error: Please run this script from the project root directory${NC}"
    exit 1
fi

# Create output directory
echo -e "${YELLOW}📁 Creating output directory: ${OUTPUT_DIR}${NC}"
mkdir -p "${OUTPUT_DIR}"

# Clean previous builds
echo -e "${YELLOW}🧹 Cleaning previous builds...${NC}"
rm -rf src-tauri/target/release/bundle
rm -rf dist
rm -rf "${OUTPUT_DIR}"/*

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}📦 Installing dependencies...${NC}"
    npm install
fi

# Build the frontend
echo -e "${YELLOW}🏗️ Building frontend...${NC}"
npm run build

# Build the Tauri app with DMG bundle
echo -e "${YELLOW}🔨 Building Tauri app with DMG bundle...${NC}"
npm run tauri build -- --bundles dmg

# Check if build was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Build completed successfully!${NC}"
    
    # Find and copy the DMG file
    DMG_PATH=$(find src-tauri/target/release/bundle/dmg -name "*.dmg" | head -n 1)
    
    if [ -f "${DMG_PATH}" ]; then
        DMG_FILENAME=$(basename "${DMG_PATH}")
        cp "${DMG_PATH}" "${OUTPUT_DIR}/${DMG_FILENAME}"
        
        echo -e "${GREEN}📦 DMG file created: ${OUTPUT_DIR}/${DMG_FILENAME}${NC}"
        echo -e "${GREEN}📊 File size: $(du -h "${OUTPUT_DIR}/${DMG_FILENAME}" | cut -f1)${NC}"
        echo -e "${BLUE}🎉 Build complete! Your DMG is ready in the ${OUTPUT_DIR} directory.${NC}"
        
        # Open the output directory
        open "${OUTPUT_DIR}"
    else
        echo -e "${RED}❌ DMG file not found in expected location${NC}"
        echo -e "${YELLOW}📁 Checking bundle directory contents:${NC}"
        ls -la src-tauri/target/release/bundle/dmg/ 2>/dev/null || echo "Bundle directory not found"
        exit 1
    fi
else
    echo -e "${RED}❌ Build failed!${NC}"
    exit 1
fi

echo -e "${BLUE}✨ All done! The macOS DMG package is ready for distribution.${NC}"