#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查 Claudia 项目中所有组件的硬编码英文文本

这个脚本会扫描所有 .tsx 文件，找出硬编码的英文字符串，
并生成需要本地化的文本列表。
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set

class I18nChecker:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.src_path = self.project_root / "src"
        
        # 英文文本模式 - 匹配引号内的英文文本
        self.text_patterns = [
            # 双引号字符串中的英文文本
            r'"([A-Z][a-zA-Z\s]{2,}[a-zA-Z])"',
            # 单引号字符串中的英文文本  
            r"'([A-Z][a-zA-Z\s]{2,}[a-zA-Z])'",
            # 模板字符串中的英文文本
            r'`([A-Z][a-zA-Z\s]{2,}[a-zA-Z])`',
            # JSX 文本内容
            r'>([A-Z][a-zA-Z\s]{2,}[a-zA-Z])<',
        ]
        
        # 需要排除的模式
        self.exclude_patterns = [
            r't\(',  # 已经使用了国际化函数
            r'useI18n',  # 国际化相关代码
            r'console\.',  # 控制台输出
            r'process\.env',  # 环境变量
            r'import.*from',  # 导入语句
            r'export.*',  # 导出语句
            r'className',  # CSS 类名
            r'data-',  # 数据属性
            r'aria-',  # 可访问性属性
            r'href=',  # 链接
            r'src=',  # 图片源
            r'id=',  # ID 属性
            r'key=',  # React key
            r'ref=',  # React ref
            r'style=',  # 样式
            r'type=',  # 类型
            r'role=',  # 角色
            r'placeholder=.*t\(',  # 已经国际化的占位符
            r'title=.*t\(',  # 已经国际化的标题
        ]
        
        # 需要排除的文件
        self.exclude_files = {
            'vite-env.d.ts',
            'main.tsx',
            'index.ts',
        }
        
        # 需要排除的目录
        self.exclude_dirs = {
            'node_modules',
            'dist',
            'build',
            '.git',
        }
        
        # 已发现的文本
        self.found_texts: Dict[str, List[Tuple[str, int, str]]] = {}
        
    def should_exclude_line(self, line: str) -> bool:
        """检查是否应该排除这一行"""
        for pattern in self.exclude_patterns:
            if re.search(pattern, line):
                return True
        return False
        
    def extract_english_texts(self, file_path: Path) -> List[Tuple[int, str, str]]:
        """从文件中提取英文文本"""
        results = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for line_num, line in enumerate(lines, 1):
                # 跳过注释行
                if line.strip().startswith('//') or line.strip().startswith('*'):
                    continue
                    
                # 跳过已经使用国际化的行
                if self.should_exclude_line(line):
                    continue
                
                # 查找英文文本
                for pattern in self.text_patterns:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        text = match.group(1)
                        # 过滤掉太短或包含特殊字符的文本
                        if (len(text) >= 3 and 
                            not text.isdigit() and
                            not re.search(r'^[A-Z_]+$', text) and  # 排除常量
                            not re.search(r'^\w+\.\w+', text) and  # 排除属性访问
                            not re.search(r'^[a-z]+://|www\.', text)):  # 排除URL
                            results.append((line_num, text, line.strip()))
                            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
            
        return results
    
    def scan_files(self):
        """扫描所有文件"""
        print("开始扫描 TypeScript/React 文件...")
        
        for file_path in self.src_path.rglob("*.tsx"):
            # 跳过排除的文件和目录
            if (file_path.name in self.exclude_files or
                any(part in self.exclude_dirs for part in file_path.parts)):
                continue
                
            print(f"扫描: {file_path.relative_to(self.project_root)}")
            
            texts = self.extract_english_texts(file_path)
            if texts:
                rel_path = str(file_path.relative_to(self.project_root))
                self.found_texts[rel_path] = texts
    
    def generate_report(self) -> str:
        """生成报告"""
        report = []
        report.append("# Claudia 项目硬编码英文文本检查报告\n")
        report.append(f"扫描时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        total_texts = sum(len(texts) for texts in self.found_texts.values())
        report.append(f"总计发现 {total_texts} 个硬编码英文文本，分布在 {len(self.found_texts)} 个文件中。\n")
        
        # 按文件分组
        report.append("## 按文件分组\n")
        for file_path, texts in sorted(self.found_texts.items()):
            report.append(f"### {file_path} ({len(texts)} 个文本)\n")
            for line_num, text, line_context in texts:
                report.append(f"- **第 {line_num} 行**: `{text}`")
                report.append(f"  ```typescript")
                report.append(f"  {line_context}")
                report.append(f"  ```\n")
        
        # 所有文本的汇总列表
        report.append("## 所有发现的文本列表\n")
        all_texts = set()
        for texts in self.found_texts.values():
            for _, text, _ in texts:
                all_texts.add(text)
        
        for text in sorted(all_texts):
            report.append(f"- {text}")
        
        # 建议的翻译键结构
        report.append("\n## 建议的翻译键结构\n")
        report.append("```json")
        report.append("{")
        
        # 按功能分组建议翻译键
        categories = self.categorize_texts(all_texts)
        for category, texts in categories.items():
            report.append(f'  "{category}": {{')
            for text in texts:
                key = self.suggest_key(text)
                report.append(f'    "{key}": "{text}",')
            report.append('  },')
        
        report.append("}")
        report.append("```")
        
        return '\n'.join(report)
    
    def categorize_texts(self, texts: Set[str]) -> Dict[str, List[str]]:
        """将文本按功能分类"""
        categories = {
            'errors': [],
            'success': [], 
            'ui': [],
            'actions': [],
            'status': [],
            'misc': []
        }
        
        for text in texts:
            text_lower = text.lower()
            if any(word in text_lower for word in ['failed', 'error', 'cannot', 'unable']):
                categories['errors'].append(text)
            elif any(word in text_lower for word in ['success', 'completed', 'saved']):
                categories['success'].append(text)
            elif any(word in text_lower for word in ['click', 'select', 'enter', 'choose']):
                categories['ui'].append(text)
            elif any(word in text_lower for word in ['create', 'delete', 'update', 'save', 'load']):
                categories['actions'].append(text)
            elif any(word in text_lower for word in ['running', 'stopped', 'active', 'pending']):
                categories['status'].append(text)
            else:
                categories['misc'].append(text)
        
        # 移除空分类
        return {k: v for k, v in categories.items() if v}
    
    def suggest_key(self, text: str) -> str:
        """建议翻译键名"""
        # 转换为驼峰命名
        words = re.sub(r'[^\w\s]', '', text).split()
        if not words:
            return 'unknown'
        
        key = words[0].lower()
        for word in words[1:]:
            key += word.capitalize()
        
        return key
    
    def generate_fixes(self) -> List[str]:
        """生成修复建议"""
        fixes = []
        fixes.append("# 修复建议\n")
        
        for file_path, texts in self.found_texts.items():
            fixes.append(f"## {file_path}\n")
            fixes.append("需要添加以下导入:")
            fixes.append("```typescript")
            fixes.append("import { useI18n } from '@/lib/i18n';")
            fixes.append("```\n")
            
            fixes.append("在组件中添加:")
            fixes.append("```typescript")
            fixes.append("const { t } = useI18n();")
            fixes.append("```\n")
            
            fixes.append("替换以下文本:")
            for line_num, text, line_context in texts:
                key = self.suggest_key(text)
                fixed_line = line_context.replace(f'"{text}"', f't("category.{key}")')
                fixed_line = fixed_line.replace(f"'{text}'", f't("category.{key}")')
                fixes.append(f"第 {line_num} 行:")
                fixes.append("```typescript")
                fixes.append(f"// 原来: {line_context}")
                fixes.append(f"// 修改为: {fixed_line}")
                fixes.append("```\n")
        
        return fixes

def main():
    # 假设脚本在项目根目录运行
    project_root = "."
    
    checker = I18nChecker(project_root)
    checker.scan_files()
    
    # 生成报告
    report = checker.generate_report()
    with open("i18n_check_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    # 生成修复建议
    fixes = checker.generate_fixes()
    with open("i18n_fixes.md", "w", encoding="utf-8") as f:
        f.write('\n'.join(fixes))
    
    print("检查完成!")
    print("报告已保存到: i18n_check_report.md")
    print("修复建议已保存到: i18n_fixes.md")
    
    # 显示简要统计
    total_texts = sum(len(texts) for texts in checker.found_texts.values())
    print(f"\n发现 {total_texts} 个硬编码英文文本，分布在 {len(checker.found_texts)} 个文件中")

if __name__ == "__main__":
    main()