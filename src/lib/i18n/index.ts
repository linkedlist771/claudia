import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import zhLocale from './locales/zh.json';
import enLocale from './locales/en.json';

export type Language = 'zh' | 'en';

export const languages = {
  zh: {
    label: '中文',
    locale: zhLocale,
    flag: '🇨🇳'
  },
  en: {
    label: 'English',
    locale: enLocale,
    flag: '🇺🇸'
  }
} as const;

interface I18nStore {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
}

// Helper function to get nested property from object
function getNestedProperty(obj: any, path: string): string {
  return path.split('.').reduce((curr, prop) => {
    return curr?.[prop] || path;
  }, obj);
}

export const useI18n = create<I18nStore>()(
  persist(
    (set, get) => ({
      language: 'zh', // Default to Chinese
      setLanguage: (lang: Language) => {
        set({ language: lang });
      },
      t: (key: string) => {
        const { language } = get();
        const locale = languages[language].locale;
        const translation = getNestedProperty(locale, key);
        
        // If translation not found, try English as fallback
        if (translation === key && language !== 'en') {
          const enTranslation = getNestedProperty(languages.en.locale, key);
          return enTranslation !== key ? enTranslation : key;
        }
        
        return translation;
      }
    }),
    {
      name: 'claudia-i18n',
      partialize: (state) => ({ language: state.language })
    }
  )
);

// Export a standalone t function for convenience
export const t = (key: string) => useI18n.getState().t(key);