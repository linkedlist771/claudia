# Windows MSI 构建指南

本文档详细介绍如何在 Windows 系统上将 Claudia 项目构建为 MSI 安装包。

## 目录
- [系统要求](#系统要求)
- [环境准备](#环境准备)
- [依赖安装](#依赖安装)
- [项目配置](#项目配置)
- [构建过程](#构建过程)
- [MSI 配置](#msi-配置)
- [打包发布](#打包发布)
- [常见问题](#常见问题)

## 系统要求

### 操作系统
- Windows 10 版本 1903 (build 18362) 或更高版本
- Windows 11 (推荐)
- 64位系统 (x64)

### 硬件要求
- 内存: 8GB RAM (推荐 16GB)
- 存储: 至少 10GB 可用空间
- 处理器: Intel Core i5 或 AMD 同等性能处理器

## 环境准备

### 1. 安装 Visual Studio Build Tools

访问 [Visual Studio 官网](https://visualstudio.microsoft.com/zh-hans/downloads/) 下载并安装：

```powershell
# 方法1: 使用 Chocolatey 安装
choco install visualstudio2022buildtools

# 方法2: 使用 winget 安装
winget install Microsoft.VisualStudio.2022.BuildTools
```

**必需的工作负载:**
- C++ 生成工具
- Windows 10/11 SDK (最新版本)
- MSVC v143 编译器工具集

### 2. 安装 Rust

```powershell
# 下载并运行 Rust 安装程序
Invoke-WebRequest -Uri "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe" -OutFile "rustup-init.exe"
.\rustup-init.exe

# 重启 PowerShell 或重新加载环境变量
refreshenv

# 验证安装
rustc --version
cargo --version
```

**配置 Rust 工具链:**
```powershell
# 安装 stable 工具链
rustup toolchain install stable-x86_64-pc-windows-msvc
rustup default stable-x86_64-pc-windows-msvc

# 安装必要的组件
rustup component add rustfmt clippy
```

### 3. 安装 Node.js

```powershell
# 方法1: 使用 Chocolatey
choco install nodejs

# 方法2: 使用 winget
winget install OpenJS.NodeJS

# 方法3: 从官网下载 LTS 版本
# https://nodejs.org/zh-cn/
```

**推荐版本:** Node.js 18 LTS 或更高版本

### 4. 安装 Tauri CLI

```powershell
# 安装 Tauri CLI
cargo install tauri-cli

# 验证安装
cargo tauri --version
```

## 依赖安装

### 1. 克隆项目
```powershell
git clone https://github.com/your-repo/claudia.git
cd claudia
```

### 2. 安装前端依赖
```powershell
# 使用 npm
npm install

# 或使用 yarn
yarn install

# 或使用 pnpm (推荐)
npm install -g pnpm
pnpm install
```

### 3. 安装 Rust 依赖
```powershell
cd src-tauri
cargo build --release
cd ..
```

## 项目配置

### 1. 配置 Tauri

编辑 `src-tauri/tauri.conf.json` 文件：

```json
{
  "package": {
    "productName": "Claudia",
    "version": "1.0.0"
  },
  "tauri": {
    "allowlist": {
      "all": false,
      "shell": {
        "all": false,
        "open": true
      },
      "fs": {
        "all": true,
        "readFile": true,
        "writeFile": true,
        "readDir": true,
        "copyFile": true,
        "createDir": true,
        "removeDir": true,
        "removeFile": true,
        "renameFile": true
      }
    },
    "bundle": {
      "active": true,
      "targets": ["msi"],
      "identifier": "com.claudia.app",
      "icon": [
        "icons/32x32.png",
        "icons/128x128.png",
        "icons/128x128@2x.png",
        "icons/icon.icns",
        "icons/icon.ico"
      ],
      "windows": {
        "certificateThumbprint": null,
        "digestAlgorithm": "sha256",
        "timestampUrl": ""
      }
    },
    "security": {
      "csp": null
    },
    "windows": [
      {
        "fullscreen": false,
        "resizable": true,
        "title": "Claudia",
        "width": 1200,
        "height": 800,
        "minWidth": 800,
        "minHeight": 600
      }
    ]
  }
}
```

### 2. 配置图标

确保在 `src-tauri/icons/` 目录下有以下图标文件：
- `32x32.png`
- `128x128.png` 
- `128x128@2x.png`
- `icon.icns` (可选)
- `icon.ico` (Windows 图标)

```powershell
# 如果没有图标，可以使用 Tauri 的图标生成工具
cargo tauri icon path/to/your/icon.png
```

### 3. 配置构建脚本

在 `package.json` 中添加构建脚本：

```json
{
  "scripts": {
    "tauri": "tauri",
    "tauri:build": "tauri build",
    "tauri:build:msi": "tauri build --target msi",
    "tauri:dev": "tauri dev",
    "build": "vite build",
    "dev": "vite"
  }
}
```

## 构建过程

### 1. 清理构建缓存
```powershell
# 清理前端构建缓存
npm run clean
# 或
rm -rf dist node_modules

# 清理 Rust 构建缓存
cd src-tauri
cargo clean
cd ..
```

### 2. 构建前端资源
```powershell
# 构建前端项目
npm run build

# 验证构建输出
ls dist/
```

### 3. 构建 Tauri 应用
```powershell
# 开发模式构建 (用于测试)
npm run tauri:dev

# 生产模式构建
npm run tauri:build

# 或者直接使用 Tauri CLI
cargo tauri build
```

## MSI 配置

### 1. WiX Toolset 安装

Tauri 使用 WiX Toolset 来创建 MSI 安装包：

```powershell
# 方法1: 使用 Chocolatey
choco install wixtoolset

# 方法2: 从官网下载
# https://wixtoolset.org/releases/
```

安装后重启 PowerShell 或重新加载环境变量。

### 2. 配置 MSI 属性

在 `src-tauri/tauri.conf.json` 中配置 MSI 相关设置：

```json
{
  "tauri": {
    "bundle": {
      "windows": {
        "wix": {
          "language": "zh-CN",
          "template": "main.wxs",
          "fragmentPaths": [],
          "componentGroupRefs": [],
          "componentRefs": [],
          "featureGroupRefs": [],
          "featureRefs": [],
          "mergeRefs": []
        }
      }
    }
  }
}
```

### 3. 自定义 WiX 模板 (可选)

创建 `src-tauri/templates/main.wxs` 文件来自定义安装程序：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Product Id="*" 
           Name="Claudia" 
           Language="2052" 
           Version="1.0.0" 
           Manufacturer="Your Company Name" 
           UpgradeCode="12345678-1234-1234-1234-123456789012">
    
    <Package InstallerVersion="200" 
             Compressed="yes" 
             InstallScope="perMachine" 
             Description="Claudia 安装程序" 
             Comments="基于 Tauri 的现代桌面应用程序" />

    <MajorUpgrade DowngradeErrorMessage="检测到更新的版本已安装。" />
    
    <Media Id="1" Cabinet="media1.cab" EmbedCab="yes" />

    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFilesFolder">
        <Directory Id="APPLICATIONFOLDER" Name="Claudia">
          <Component Id="MainExecutable" Guid="*">
            <File Id="ClaudiaEXE" 
                  Source="$(var.CargoTargetBinDir)\claudia.exe" 
                  KeyPath="yes" 
                  Checksum="yes"/>
            <Shortcut Id="ApplicationStartMenuShortcut" 
                      Name="Claudia" 
                      Directory="ProgramMenuFolder" 
                      WorkingDirectory="APPLICATIONFOLDER" 
                      Icon="ProductIcon"/>
          </Component>
        </Directory>
      </Directory>
      <Directory Id="ProgramMenuFolder">
        <Directory Id="ApplicationProgramsFolder" Name="Claudia"/>
      </Directory>
    </Directory>

    <Icon Id="ProductIcon" SourceFile="icons\icon.ico"/>
    <Property Id="ARPPRODUCTICON" Value="ProductIcon"/>

    <Feature Id="MainApplication" Title="主程序" Level="1">
      <ComponentRef Id="MainExecutable"/>
    </Feature>
  </Product>
</Wix>
```

## 打包发布

### 1. 执行构建命令
```powershell
# 确保环境变量正确设置
$env:TAURI_PRIVATE_KEY = "your-private-key"
$env:TAURI_KEY_PASSWORD = "your-key-password"

# 执行构建
npm run tauri:build
```

### 2. 查找构建产物
```powershell
# MSI 文件位置
ls src-tauri\target\release\bundle\msi\

# 典型输出文件名
# Claudia_1.0.0_x64_zh-CN.msi
```

### 3. 验证 MSI 包
```powershell
# 安装测试
Start-Process -FilePath "src-tauri\target\release\bundle\msi\Claudia_1.0.0_x64_zh-CN.msi" -Verb RunAs

# 或者使用 msiexec 进行静默安装测试
msiexec /i "src-tauri\target\release\bundle\msi\Claudia_1.0.0_x64_zh-CN.msi" /quiet /l*v install.log
```

### 4. 代码签名 (可选但推荐)

```powershell
# 使用 signtool 对 MSI 进行签名
signtool sign /f certificate.pfx /p password /t http://timestamp.verisign.com/scripts/timstamp.dll "src-tauri\target\release\bundle\msi\Claudia_1.0.0_x64_zh-CN.msi"
```

## 自动化构建脚本

创建 `build-msi.ps1` 脚本来自动化整个构建过程：

```powershell
# build-msi.ps1
param(
    [string]$Version = "1.0.0",
    [switch]$Clean = $false,
    [switch]$Sign = $false
)

Write-Host "开始构建 Claudia MSI 安装包..." -ForegroundColor Green

# 清理构建缓存
if ($Clean) {
    Write-Host "清理构建缓存..." -ForegroundColor Yellow
    Remove-Item -Path "dist" -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path "node_modules" -Recurse -Force -ErrorAction SilentlyContinue
    Set-Location "src-tauri"
    cargo clean
    Set-Location ".."
}

# 安装依赖
Write-Host "安装前端依赖..." -ForegroundColor Yellow
npm install

# 构建前端
Write-Host "构建前端资源..." -ForegroundColor Yellow
npm run build

# 构建 Tauri 应用
Write-Host "构建 Tauri 应用..." -ForegroundColor Yellow
cargo tauri build

# 检查构建结果
$msiPath = "src-tauri\target\release\bundle\msi\Claudia_${Version}_x64_zh-CN.msi"
if (Test-Path $msiPath) {
    Write-Host "构建成功! MSI 文件位置: $msiPath" -ForegroundColor Green
    
    # 代码签名
    if ($Sign -and $env:SIGN_CERTIFICATE) {
        Write-Host "对 MSI 进行代码签名..." -ForegroundColor Yellow
        signtool sign /f $env:SIGN_CERTIFICATE /p $env:SIGN_PASSWORD /t http://timestamp.verisign.com/scripts/timstamp.dll $msiPath
    }
    
    # 显示文件信息
    Get-ItemProperty $msiPath | Select-Object Name, Length, LastWriteTime
} else {
    Write-Host "构建失败! MSI 文件未找到。" -ForegroundColor Red
    exit 1
}

Write-Host "构建完成!" -ForegroundColor Green
```

使用方法：
```powershell
# 普通构建
.\build-msi.ps1

# 清理构建
.\build-msi.ps1 -Clean

# 构建并签名
.\build-msi.ps1 -Sign

# 指定版本号
.\build-msi.ps1 -Version "1.2.0"
```

## 常见问题

### 1. Rust 编译错误

**问题:** `error: Microsoft Visual C++ 14.0 is required`

**解决方案:**
```powershell
# 安装 Visual Studio Build Tools
winget install Microsoft.VisualStudio.2022.BuildTools

# 或者安装完整的 Visual Studio Community
winget install Microsoft.VisualStudio.2022.Community
```

### 2. Node.js 版本问题

**问题:** `Node version not supported`

**解决方案:**
```powershell
# 使用 nvm-windows 管理 Node.js 版本
winget install CoreyButler.NVMforWindows

# 安装并使用 LTS 版本
nvm install lts
nvm use lts
```

### 3. WiX Toolset 问题

**问题:** `WiX Toolset not found`

**解决方案:**
```powershell
# 重新安装 WiX Toolset
choco uninstall wixtoolset
choco install wixtoolset

# 或者手动添加到 PATH
$env:PATH += ";C:\Program Files (x86)\WiX Toolset v3.11\bin"
```

### 4. 内存不足问题

**问题:** 构建过程中内存不足

**解决方案:**
```powershell
# 增加 Node.js 内存限制
$env:NODE_OPTIONS = "--max-old-space-size=8192"

# 或者在 package.json 中设置
{
  "scripts": {
    "build": "node --max-old-space-size=8192 node_modules/vite/bin/vite.js build"
  }
}
```

### 5. 权限问题

**问题:** `Access denied` 或权限不足

**解决方案:**
```powershell
# 以管理员身份运行 PowerShell
Start-Process PowerShell -Verb RunAs

# 或者修改执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 6. 网络问题

**问题:** 依赖下载失败

**解决方案:**
```powershell
# 配置 npm 镜像
npm config set registry https://registry.npmmirror.com

# 配置 Rust 镜像
# 在 ~/.cargo/config.toml 中添加:
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```

## 发布准备

### 1. 创建发布包

```powershell
# 创建发布目录
mkdir release
Copy-Item "src-tauri\target\release\bundle\msi\*.msi" -Destination "release\"

# 创建校验和文件
Get-FileHash "release\*.msi" -Algorithm SHA256 | Out-File "release\checksums.txt"
```

### 2. 文档准备

确保包含以下文档：
- `README.md` - 项目说明
- `CHANGELOG.md` - 版本更新日志
- `LICENSE` - 许可证文件
- `INSTALL.md` - 安装说明

### 3. 测试清单

发布前确保完成以下测试：
- [ ] 全新安装测试
- [ ] 升级安装测试
- [ ] 卸载测试
- [ ] 功能完整性测试
- [ ] 不同 Windows 版本兼容性测试
- [ ] 杀毒软件扫描测试

## 维护和更新

### 1. 版本管理

```powershell
# 更新版本号
npm version patch  # 1.0.0 -> 1.0.1
npm version minor  # 1.0.0 -> 1.1.0
npm version major  # 1.0.0 -> 2.0.0
```

### 2. 自动更新配置

在 `tauri.conf.json` 中配置自动更新：

```json
{
  "updater": {
    "active": true,
    "endpoints": ["https://your-domain.com/updates/{{target}}/{{current_version}}"],
    "dialog": true,
    "pubkey": "your-public-key"
  }
}
```

这个详细的构建指南应该能帮助您在 Windows 系统上成功构建 Claudia 的 MSI 安装包。如果遇到任何问题，请参考常见问题部分或查看相关的错误日志。