import React from 'react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from './ui/dropdown-menu';
import { Button } from './ui/button';
import { useI18n, languages, type Language } from '@/lib/i18n';

// 文A 图标组件
const LanguageIcon = () => (
  <svg
    width="16"
    height="16"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className="h-4 w-4"
  >
    <text
      x="12"
      y="16"
      textAnchor="middle"
      fontSize="14"
      fontWeight="bold"
      fill="currentColor"
      fontFamily="sans-serif"
    >
      文A
    </text>
  </svg>
);

export function LanguageSelector() {
  const { language, setLanguage } = useI18n();

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon" className="h-8 w-8">
          <LanguageIcon />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        {(Object.keys(languages) as Language[]).map((lang) => (
          <DropdownMenuItem
            key={lang}
            onClick={() => setLanguage(lang)}
            className="flex items-center gap-2"
          >
            <span className="text-lg">{languages[lang].flag}</span>
            <span className={language === lang ? 'font-semibold' : ''}>
              {languages[lang].label}
            </span>
            {language === lang && (
              <span className="ml-auto text-xs">✓</span>
            )}
          </DropdownMenuItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}