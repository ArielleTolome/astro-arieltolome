// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
	site: 'https://astro.arieltolome.com',
	integrations: [sitemap()],
});
