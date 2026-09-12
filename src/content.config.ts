import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const CATEGORIES = [
	'Beverages',
	'Breakfast',
	'Main Course',
	'Salads',
	'Smoothies',
	'Snacks',
	'Soups',
	'Sweet Treats',
] as const;

export function categorySlug(category: string) {
	return category.toLowerCase().replace(/\s+/g, '-');
}

const recipes = defineCollection({
	loader: glob({ pattern: '**/*.md', base: './src/content/recipes' }),
	schema: z.object({
		title: z.string(),
		category: z.enum(CATEGORIES),
		description: z.string(),
		pubDate: z.coerce.date(),
		prepTime: z.string(),
		servings: z.number(),
		cuisine: z.string(),
		accent: z.string(),
	}),
});

export const collections = { recipes };
