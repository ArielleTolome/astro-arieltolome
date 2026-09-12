#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "src/content/recipes"
PROMPTS = ROOT / "scripts/image-batches"
ACCENTS = ["#e6ecd5", "#fceace", "#b2cee7", "#c3cda7"]

# slug, title, category, description, date, prep, servings, cuisine, intro, ingredients, steps, photo
DATA = [
("hibiscus-lime-cooler", "Hibiscus Lime Cooler", "Beverages", "Tart hibiscus tea over ice with a lot of lime.", "2026-08-01", "15 mins", 4, "Mexican-inspired",
 "Brew the flowers strong. Lime keeps it from tasting like perfume.",
 ["1/2 cup dried hibiscus", "4 cups water", "2 limes, juiced", "2 tbsp sugar", "Ice"],
 ["Simmer hibiscus in water 10 minutes. Strain and cool.", "Stir in lime and sugar.", "Pour over ice."],
 "A pitcher and glass of deep ruby hibiscus cooler over ice, lime wheels floating, condensation on the glass, bright window light."),
("turmeric-golden-tonic", "Turmeric Golden Tonic", "Beverages", "Warm turmeric, ginger, and black pepper in oat milk.", "2026-07-22", "10 mins", 2, "Indian-inspired",
 "Black pepper is not optional; it wakes the turmeric up.",
 ["2 cups oat milk", "1 tsp turmeric", "1 inch ginger, grated", "1 tsp honey", "Pinch black pepper"],
 ["Warm oat milk with turmeric, ginger, and pepper. Do not boil.", "Sweeten with honey.", "Pour into mugs."],
 "Two mugs of golden turmeric tonic, fine pepper flecks, steam, honey dipper, warm side light on ceramic."),
("cucumber-basil-agua-fresca", "Cucumber Basil Agua Fresca", "Beverages", "Blended cucumber, basil, and lime, strained cold.", "2026-07-11", "10 mins", 4, "Mexican-inspired",
 "Strain it or it tastes like salad water. The basil goes in at the end.",
 ["2 cucumbers, peeled", "1 lime, juiced", "8 basil leaves", "2 tbsp sugar", "3 cups cold water"],
 ["Blend cucumber, water, sugar, and lime.", "Strain through a fine mesh.", "Tear in basil and chill."],
 "A pale green cucumber agua fresca in a tall glass with basil sprigs, ice, cucumber ribbon garnish, airy daylight."),
("salted-watermelon-shrub", "Salted Watermelon Shrub", "Beverages", "Watermelon vinegar shrub lengthened with soda.", "2026-06-28", "20 mins", 6, "American",
 "The salt is what makes it taste like fruit instead of candy.",
 ["4 cups watermelon, cubed", "1/2 cup apple cider vinegar", "1/3 cup sugar", "1 tsp sea salt", "Soda water"],
 ["Macerate watermelon with sugar and salt 15 minutes.", "Stir in vinegar, strain.", "Serve 1 part shrub to 3 parts soda."],
 "A pink watermelon shrub highball with soda bubbles, salt crystals on the rim, watermelon cube skewer, photoreal."),
("iced-cardamom-coffee", "Iced Cardamom Coffee", "Beverages", "Cold brew shaken with crushed cardamom and oat milk.", "2026-06-09", "8 mins", 2, "Levantine-inspired",
 "Crush the pods, don’t powder them, or it turns dusty.",
 ["1 cup strong cold brew", "4 cardamom pods, crushed", "1/2 cup oat milk", "Ice", "1 tsp maple"],
 ["Shake cold brew, cardamom, maple, and ice 20 seconds.", "Strain over fresh ice.", "Top with oat milk."],
 "Iced cardamom coffee in a short glass, oat-milk swirl, cracked pods on linen, condensation, cafe window light."),
("roasted-barley-tea", "Roasted Barley Tea", "Beverages", "Toasted barley simmered until nutty and clear.", "2026-05-30", "20 mins", 4, "Korean",
 "Toast until it smells like popcorn. That’s the whole recipe.",
 ["1/2 cup hulled barley", "6 cups water", "Pinch salt"],
 ["Toast barley in a dry pot until deep brown and fragrant.", "Add water, simmer 15 minutes.", "Strain. Drink hot or iced."],
 "A glass pot and cups of amber roasted barley tea, toasted grains in a small dish, steam, quiet kitchen light."),
("savory-oat-congee", "Savory Oat Congee", "Breakfast", "Oats cooked like rice porridge with ginger and soy.", "2026-08-03", "25 mins", 2, "Chinese-inspired",
 "Keep stirring. The oats should slump, not sit in lumps.",
 ["1 cup rolled oats", "4 cups water", "1 inch ginger", "1 tbsp soy sauce", "Scallions", "Sesame oil"],
 ["Simmer oats, water, and ginger 20 minutes, stirring.", "Season with soy.", "Finish with scallion and sesame oil."],
 "A bowl of savory oat congee, scallion threads, sesame oil sheen, steam, ceramic spoon, morning light."),
("almond-ricotta-toast", "Almond Ricotta Toast", "Breakfast", "Thick toast, whipped almond ricotta, honey, and pepper.", "2026-07-19", "10 mins", 2, "American",
 "The pepper on honey is the whole point.",
 ["2 thick slices sourdough", "1/2 cup almond ricotta", "1 tbsp honey", "Black pepper", "Olive oil"],
 ["Toast the bread hard.", "Spread ricotta, drizzle honey and oil.", "Crack pepper over the top."],
 "Sourdough toast piled with almond ricotta, honey drip, cracked pepper, olive oil gloss, 45-degree cookbook shot."),
("sweet-potato-hash", "Sweet Potato Hash", "Breakfast", "Crisp sweet potato, onion, and smoked paprika in a skillet.", "2026-07-05", "30 mins", 3, "American",
 "Don’t crowd the pan or it steams. You want brown edges.",
 ["2 sweet potatoes, diced", "1 onion, sliced", "1 tsp smoked paprika", "2 tbsp oil", "Salt"],
 ["Heat oil until it shimmers. Add potato in one layer.", "Leave it 4 minutes before stirring.", "Add onion and paprika, cook until both are browned."],
 "A cast-iron skillet of browned sweet potato hash, paprika, caramelized onion, steam, rustic table."),
("coconut-chia-jars", "Coconut Chia Jars", "Breakfast", "Overnight chia in coconut milk with mango.", "2026-06-16", "10 mins", 2, "American",
 "Stir twice in the first ten minutes or you get a clump.",
 ["1/4 cup chia seeds", "1 cup coconut milk", "1 tbsp maple", "1 mango, diced", "Pinch salt"],
 ["Stir chia, coconut milk, maple, and salt.", "Wait 10 minutes, stir again, chill overnight.", "Top with mango."],
 "Two glass jars of coconut chia pudding topped with diced mango, coconut milk sheen, bright breakfast light."),
("herb-scramble-wrap", "Herb Scramble Wrap", "Breakfast", "Soft tofu scramble, herbs, and hot sauce in a tortilla.", "2026-05-24", "15 mins", 2, "American",
 "Pull it off the heat while it still looks wet. It keeps cooking.",
 ["8 oz firm tofu, crumbled", "1 tbsp nutritional yeast", "Handful parsley and chives", "2 tortillas", "Hot sauce"],
 ["Cook tofu in a slick of oil with yeast and salt until just set.", "Fold in herbs off heat.", "Wrap in warm tortillas with hot sauce."],
 "A cut breakfast wrap showing yellow herb tofu scramble, tortilla, hot sauce dots, photoreal, appetizing."),
("buckwheat-banana-hotcakes", "Buckwheat Banana Hotcakes", "Breakfast", "Savory-sweet buckwheat pancakes with caramelized banana.", "2026-04-30", "25 mins", 3, "American",
 "Buckwheat browns fast. Medium heat, not high.",
 ["1 cup buckwheat flour", "1 cup oat milk", "1 egg or flax egg", "2 bananas", "Butter or oil"],
 ["Whisk flour, milk, and egg. Rest 5 minutes.", "Cook small cakes until bubbles set.", "Fry banana slices in the same pan and stack them on top."],
 "A stack of buckwheat pancakes with caramelized banana, maple sheen, butter melt, steam, cookbook lighting."),
("miso-glazed-eggplant", "Miso Glazed Eggplant", "Main Course", "Broiled eggplant with a sweet-salty miso lacquer.", "2026-08-08", "30 mins", 4, "Japanese",
 "The glaze should blister, not burn. Watch the last two minutes.",
 ["2 globe eggplants, halved", "2 tbsp white miso", "1 tbsp mirin", "1 tsp sugar", "Sesame seeds"],
 ["Score eggplant, brush with oil, roast 20 minutes at 425°F.", "Mix miso, mirin, sugar. Brush on.", "Broil 2 minutes. Sesame on top."],
 "Roasted eggplant halves with blistered miso glaze, sesame, charred edges, glistening, 45-degree food photo."),
("chickpea-coconut-stew", "Chickpea Coconut Stew", "Main Course", "Chickpeas in coconut milk with tomato and turmeric.", "2026-07-28", "35 mins", 4, "West African-inspired",
 "Let it reduce until the oil starts to separate. That’s when it tastes finished.",
 ["2 cans chickpeas", "1 can coconut milk", "1 cup crushed tomato", "1 tsp turmeric", "1 onion"],
 ["Soften onion in oil. Add turmeric.", "Add tomato, coconut milk, chickpeas.", "Simmer 20 minutes until thick."],
 "A pot of chickpea coconut stew, orange-gold sauce, chickpeas, cilantro, steam, rich and glossy."),
("mushroom-farro-skillet", "Mushroom Farro Skillet", "Main Course", "Farro, browned mushrooms, and thyme in one pan.", "2026-07-08", "40 mins", 4, "Italian-inspired",
 "Brown the mushrooms hard before the farro goes in.",
 ["1 cup farro", "1 lb mixed mushrooms", "1 onion", "Thyme", "3 cups broth"],
 ["Sear mushrooms in oil until they squeak. Set aside.", "Toast farro with onion, add broth, simmer 25 minutes.", "Fold mushrooms and thyme back in."],
 "A skillet of mushroom farro, seared mushrooms, thyme sprigs, broth gloss, photoreal savory steam."),
("sheet-pan-harissa-tofu", "Sheet-Pan Harissa Tofu", "Main Course", "Tofu and vegetables roasted in harissa oil.", "2026-06-20", "35 mins", 4, "North African-inspired",
 "Press the tofu or it won’t take color.",
 ["1 block extra-firm tofu", "2 tbsp harissa", "1 tbsp oil", "1 red onion", "1 zucchini"],
 ["Heat oven to 425°F. Toss everything with harissa and oil.", "Spread out. Roast 25 minutes, flipping once.", "Salt at the end."],
 "A sheet pan of harissa-roasted tofu cubes and vegetables, charred edges, red oil, steam, overhead 45-degree."),
("lemon-herb-white-beans", "Lemon Herb White Beans", "Main Course", "Simmered white beans with lemon, garlic, and parsley.", "2026-06-02", "25 mins", 4, "Italian",
 "Use the bean liquid. That’s the sauce.",
 ["2 cans cannellini, not drained", "4 garlic cloves", "1 lemon", "Parsley", "Olive oil", "Chili flakes"],
 ["Warm garlic in a lot of oil.", "Add beans and their liquid, simmer 10 minutes.", "Off heat: lemon zest, juice, parsley, chili."],
 "A shallow bowl of lemon herb white beans, olive oil pool, parsley, lemon zest, crusty bread at the edge."),
("peanut-soba-noodles", "Peanut Soba Noodles", "Main Course", "Cold soba with a sharp peanut-lime sauce.", "2026-05-15", "20 mins", 3, "Japanese-inspired",
 "Rinse the noodles cold or they glue together.",
 ["8 oz soba", "3 tbsp peanut butter", "1 lime", "1 tbsp soy", "1 tsp sesame oil", "Cucumber"],
 ["Boil soba, rinse under cold water.", "Whisk peanut butter, lime, soy, sesame, splash of water.", "Toss with noodles and cucumber."],
 "A bowl of peanut soba noodles, glossy sauce, cucumber matchsticks, lime, chopsticks, photoreal."),
("roasted-cauliflower-tacos", "Roasted Cauliflower Tacos", "Main Course", "Charred cauliflower, slaw, and lime crema.", "2026-04-18", "35 mins", 4, "Mexican-inspired",
 "The cauliflower should look almost burnt on the edges.",
 ["1 head cauliflower", "2 tsp cumin", "8 tortillas", "Cabbage slaw", "Lime yogurt"],
 ["Roast cauliflower with cumin and oil at 450°F for 25 minutes.", "Warm tortillas.", "Fill with cauliflower, slaw, crema."],
 "Three cauliflower tacos on a plate, charred florets, slaw, lime crema drizzle, cilantro, street-food cookbook."),
("tomato-olive-orzo", "Tomato Olive Orzo", "Main Course", "Orzo cooked like risotto with tomatoes and olives.", "2026-03-22", "30 mins", 4, "Greek-inspired",
 "Don’t drain a thing. Starchy water is the cream.",
 ["1 cup orzo", "1 pint cherry tomatoes", "1/2 cup olives", "2 garlic cloves", "2 cups broth"],
 ["Sizzle garlic and tomatoes until they burst.", "Add orzo, toast 1 minute, add broth.", "Stir until creamy. Fold in olives."],
 "A pan of tomato olive orzo, burst cherry tomatoes, olives, glossy starch, basil, photoreal Italian-Greek."),
("grilled-peach-farro-salad", "Grilled Peach Farro Salad", "Salads", "Farro, grilled peaches, and a sharp vinaigrette.", "2026-08-06", "30 mins", 4, "American",
 "Grill the peaches cut-side down until they stripe.",
 ["1 cup farro, cooked", "3 peaches, halved", "Arugula", "1 tbsp vinegar", "Olive oil"],
 ["Grill peaches 3 minutes.", "Toss farro with oil, vinegar, salt.", "Add arugula and sliced peaches."],
 "A platter of grilled peach farro salad, caramelized peach halves, arugula, farro, vinaigrette shine."),
("smashed-cucumber-sesame", "Smashed Cucumber Sesame", "Salads", "Smashed cucumbers, garlic, vinegar, and sesame.", "2026-07-14", "15 mins", 4, "Chinese",
 "Smash, don’t slice. You want ragged edges that hold sauce.",
 ["4 cucumbers", "2 garlic cloves", "1 tbsp rice vinegar", "1 tsp sesame oil", "Chili crisp"],
 ["Smash cucumbers under a knife, tear into chunks, salt 10 minutes.", "Drain. Toss with garlic, vinegar, sesame.", "Chili crisp on top."],
 "A bowl of smashed cucumber salad, sesame oil, chili crisp, garlic, jagged cucumber pieces, photoreal."),
("roasted-beet-walnut", "Roasted Beet Walnut Salad", "Salads", "Roasted beets, toasted walnuts, and orange.", "2026-06-07", "50 mins", 4, "American",
 "Foil-roast the beets so they steam in their own juice.",
 ["4 beets", "1/2 cup walnuts", "1 orange", "Olive oil", "Salt"],
 ["Wrap beets, roast 40 minutes at 400°F. Peel.", "Toast walnuts.", "Slice beets, dress with orange juice and oil, walnuts on top."],
 "Roasted beet salad with walnuts and orange segments, deep magenta, oil sheen, rustic plate."),
("fennel-orange-salad", "Fennel Orange Salad", "Salads", "Shaved fennel, orange, and olive oil. That’s it.", "2026-05-03", "15 mins", 4, "Italian",
 "Shave the fennel paper-thin or it tastes like raw onion.",
 ["2 fennel bulbs", "2 oranges", "Olive oil", "Salt", "Fennel fronds"],
 ["Shave fennel on a mandoline.", "Segment oranges over the bowl so juice falls in.", "Oil, salt, fronds."],
 "A white platter of shaved fennel and orange salad, olive oil, fronds, bright citrus, photoreal."),
("charred-broccoli-tahini", "Charred Broccoli Tahini", "Salads", "Almost-burnt broccoli with lemon tahini.", "2026-04-09", "25 mins", 4, "Levantine-inspired",
 "If it still looks green and polite, it isn’t done.",
 ["2 heads broccoli", "3 tbsp tahini", "1 lemon", "Garlic", "Oil"],
 ["Roast broccoli at 450°F until charred, 20 minutes.", "Whisk tahini, lemon, garlic, water until pourable.", "Spoon sauce over broccoli."],
 "Charred broccoli on a platter, lemon tahini drizzle, burnt florets, sesame, photoreal savory."),
("tomato-bread-panzanella", "Tomato Bread Panzanella", "Salads", "Ripe tomatoes soaking toasted bread.", "2026-08-20", "25 mins", 4, "Italian",
 "Salt the tomatoes first and use that juice as dressing.",
 ["2 lb ripe tomatoes", "4 cups toasted bread cubes", "Basil", "Red wine vinegar", "Olive oil"],
 ["Salt chopped tomatoes 10 minutes. Save the juice.", "Toss juice with oil and vinegar.", "Add bread and basil. Rest 10 minutes."],
 "A bowl of panzanella, juicy tomatoes, soaked bread cubes, basil, olive oil, summer light."),
("mango-lime-lassi", "Mango Lime Lassi", "Smoothies", "Mango, yogurt, lime, and a pinch of salt.", "2026-08-04", "5 mins", 2, "Indian",
 "The salt is what makes it taste like mango, not dessert.",
 ["2 cups mango", "1 cup yogurt", "1 lime", "Pinch salt", "Ice"],
 ["Blend everything until smooth.", "Taste for salt.", "Serve immediately."],
 "A glass of thick mango lassi, saffron-orange, lime wedge, yogurt swirl, condensation, photoreal."),
("blueberry-oat-shake", "Blueberry Oat Shake", "Smoothies", "Frozen blueberries blended with oats and milk.", "2026-07-16", "5 mins", 1, "American",
 "The oats make it drink like breakfast, not juice.",
 ["1 cup frozen blueberries", "1/4 cup oats", "1 cup oat milk", "1 tsp maple"],
 ["Blend until the oats disappear.", "Drink cold."],
 "A purple blueberry oat shake in a glass, oat milk, berries on top, thick texture, morning light."),
("cacao-date-smoothie", "Cacao Date Smoothie", "Smoothies", "Dates, cacao, and almond milk. Dessert for breakfast.", "2026-06-11", "5 mins", 1, "American",
 "Soak the dates if they’re stiff or you’ll get flecks.",
 ["4 dates, pitted", "1 tbsp cacao", "1 cup almond milk", "1 banana", "Pinch salt"],
 ["Blend until completely smooth.", "Pour. No garnish required."],
 "A chocolate-brown cacao date smoothie, thick, cacao dust, dates nearby, photoreal dessert-breakfast."),
("carrot-ginger-glow", "Carrot Ginger Glow", "Smoothies", "Carrot, orange, ginger, and a knob of turmeric.", "2026-05-08", "8 mins", 2, "American",
 "Fresh carrot, not juice from a bottle, or it tastes thin.",
 ["3 carrots, chopped", "1 orange", "1 inch ginger", "1/2 tsp turmeric", "Water"],
 ["Blend with a splash of water until it moves.", "Strain if you hate pulp. Don’t if you don’t."],
 "A vivid orange carrot-ginger smoothie, turmeric flecks, ginger slice, bright daylight, photoreal."),
("frozen-grape-mint", "Frozen Grape Mint Smoothie", "Smoothies", "Frozen grapes and mint. It tastes like a sorbet.", "2026-04-12", "5 mins", 1, "American",
 "Freeze the grapes ahead. That’s the whole trick.",
 ["2 cups frozen grapes", "8 mint leaves", "Splash of water", "Squeeze of lemon"],
 ["Blend grapes and mint. Add water to catch the blades.", "Lemon at the end."],
 "A pale purple frozen grape mint smoothie, mint sprig, frosty glass, photoreal, refreshing."),
("avocado-matcha-shake", "Avocado Matcha Shake", "Smoothies", "Avocado, matcha, and cold milk. Green and thick.", "2026-03-08", "5 mins", 1, "Japanese-inspired",
 "Sift the matcha or it clumps.",
 ["1/2 avocado", "1 tsp matcha", "1 cup cold milk", "1 tsp honey"],
 ["Blend avocado, milk, honey.", "Sift matcha on top and blend 5 more seconds."],
 "A creamy avocado matcha shake, pale green, matcha dust, thick texture, ceramic cup, photoreal."),
("zaatar-pita-chips", "Za'atar Pita Chips", "Snacks", "Torn pita baked with olive oil and za'atar.", "2026-08-09", "15 mins", 4, "Levantine",
 "Tear, don’t cut. Ragged edges brown better.",
 ["4 pitas", "3 tbsp olive oil", "2 tbsp za'atar", "Salt"],
 ["Heat oven to 400°F. Tear pita, toss with oil, za'atar, salt.", "Bake 10 minutes until crisp."],
 "A pile of za'atar pita chips, olive oil sheen, herb dust, golden edges, snack-bowl cookbook shot."),
("spicy-edamame", "Spicy Edamame", "Snacks", "Hot edamame tossed with chili and flaky salt.", "2026-07-21", "10 mins", 3, "Japanese",
 "Salt them while they steam so it sticks.",
 ["1 lb frozen edamame in pods", "1 tsp chili flakes", "Flaky salt", "Sesame oil"],
 ["Steam or boil edamame 5 minutes.", "Toss with chili, salt, sesame oil.", "Serve in a bowl you can throw the pods into."],
 "A bowl of spicy edamame in pods, chili flakes, flaky salt, steam, photoreal bar snack."),
("olive-oil-popcorn", "Olive Oil Popcorn", "Snacks", "Stovetop popcorn, olive oil, and too much pepper.", "2026-06-25", "10 mins", 4, "American",
 "The oil goes in after popping so it doesn’t scorch.",
 ["1/2 cup popcorn kernels", "3 tbsp olive oil", "Black pepper", "Salt"],
 ["Pop kernels in 1 tbsp oil with a lid.", "Drizzle remaining oil.", "Salt and a lot of pepper."],
 "A bowl of olive oil popcorn, pepper, salt crystals, golden kernels, photoreal snack."),
("white-bean-dip", "White Bean Dip", "Snacks", "Blended white beans, lemon, and a puddle of oil.", "2026-05-19", "10 mins", 6, "Mediterranean",
 "Keep it thick. Thin dips taste like baby food.",
 ["1 can white beans", "1 lemon", "1 garlic clove", "Olive oil", "Salt"],
 ["Blend beans, garlic, lemon, salt, 2 tbsp oil.", "Spoon into a bowl, well in the center, more oil."],
 "White bean dip in a shallow bowl, olive oil well, lemon, pita, photoreal mezze."),
("maple-pepitas", "Maple Pepitas", "Snacks", "Pumpkin seeds toasted with maple and chili.", "2026-04-02", "15 mins", 8, "American",
 "Pull them when they look wet. They crisp as they cool.",
 ["2 cups pepitas", "2 tbsp maple", "1/2 tsp chili", "Salt"],
 ["Toss pepitas with maple, chili, salt.", "Toast in a skillet, stirring, 6 minutes.", "Cool on a plate."],
 "A bowl of maple chili pepitas, glossy, chili dust, scattered seeds on linen, photoreal."),
("cucumber-chili-spears", "Cucumber Chili Spears", "Snacks", "Cucumber spears, chili oil, and flaky salt.", "2026-03-11", "8 mins", 2, "Sichuan-inspired",
 "Salt, wait, drain. Then chili. Otherwise it waters down.",
 ["2 cucumbers", "1 tsp chili oil", "Flaky salt", "Vinegar splash"],
 ["Cut spears, salt 5 minutes, pat dry.", "Toss with chili oil and vinegar."],
 "Cucumber spears on a plate, chili oil, flaky salt, photoreal cold snack."),
("tomato-fennel-broth", "Tomato Fennel Broth", "Soups", "A clear-ish tomato broth with shaved fennel.", "2026-08-11", "40 mins", 4, "Italian",
 "Don’t blend this one. You want to see through it a little.",
 ["1 lb tomatoes", "1 fennel bulb", "4 cups water", "Garlic", "Olive oil"],
 ["Simmer tomatoes, garlic, water 25 minutes. Strain.", "Add shaved fennel to the hot broth.", "Oil and salt."],
 "A bowl of tomato fennel broth, translucent red, fennel shards, oil droplets, steam, photoreal."),
("red-lentil-lemon", "Red Lentil Lemon Soup", "Soups", "Red lentils, cumin, and a lot of lemon.", "2026-07-03", "30 mins", 4, "Levantine",
 "It looks ugly until the lemon goes in. Then it tastes finished.",
 ["1 cup red lentils", "1 onion", "1 tsp cumin", "1 lemon", "5 cups water"],
 ["Cook onion, cumin, lentils, water 20 minutes.", "Blend half.", "Lemon juice, more than you think."],
 "A bowl of red lentil lemon soup, cumin, lemon wedge, olive oil, steam, photoreal."),
("miso-mushroom-soup", "Miso Mushroom Soup", "Soups", "Mushroom broth finished with miso off the heat.", "2026-06-05", "25 mins", 4, "Japanese",
 "Boiling miso kills it. Stir it in a ladle of broth first.",
 ["8 oz mushrooms", "4 cups water", "2 tbsp miso", "Tofu cubes", "Scallion"],
 ["Simmer mushrooms in water 15 minutes.", "Ladle broth into miso, then return.", "Add tofu and scallion."],
 "Miso mushroom soup in a bowl, tofu, scallion, mushroom slices, steam, photoreal Japanese."),
("roasted-carrot-ginger", "Roasted Carrot Ginger Soup", "Soups", "Roasted carrots blended with ginger and coconut.", "2026-05-01", "45 mins", 4, "American",
 "Roast until the edges almost burn. That’s the sweetness.",
 ["2 lb carrots", "1 onion", "1 inch ginger", "1 can coconut milk", "Broth"],
 ["Roast carrots and onion at 425°F for 30 minutes.", "Blend with ginger, coconut milk, broth.", "Salt."],
 "A bowl of roasted carrot ginger soup, deep orange, coconut swirl, ginger, steam, photoreal."),
("green-minestrone", "Green Minestrone", "Soups", "A spring minestrone of beans, greens, and pasta.", "2026-04-07", "35 mins", 4, "Italian",
 "Add the greens at the end so they stay loud.",
 ["1 can white beans", "2 cups chopped greens", "1/2 cup small pasta", "Garlic", "Parmesan rind or lemon"],
 ["Sauté garlic, add beans and water, simmer.", "Cook pasta in the pot.", "Stir in greens 2 minutes."],
 "A bowl of green minestrone, beans, pasta, wilted greens, olive oil, photoreal spring soup."),
("black-bean-chipotle", "Black Bean Chipotle Soup", "Soups", "Black beans, chipotle, and lime. Blended half-smooth.", "2026-03-03", "30 mins", 4, "Mexican-inspired",
 "One chipotle is enough. Two if you mean it.",
 ["2 cans black beans", "1 chipotle in adobo", "1 onion", "Lime", "Cumin"],
 ["Cook onion, cumin, chipotle.", "Add beans and water, simmer 15 minutes.", "Blend half, lime at the end."],
 "Black bean chipotle soup, dark, lime crema swirl, cilantro, steam, photoreal."),
("olive-oil-citrus-cake", "Olive Oil Citrus Cake", "Sweet Treats", "A damp olive-oil cake with orange zest.", "2026-08-14", "55 mins", 8, "Italian",
 "It should look underbaked in the middle. It isn’t.",
 ["1 cup sugar", "3 eggs", "3/4 cup olive oil", "1 orange, zested and juiced", "1 1/2 cups flour"],
 ["Whisk sugar, eggs, oil, orange.", "Fold in flour and a pinch of salt.", "Bake 350°F about 40 minutes."],
 "A sliced olive oil citrus cake, moist crumb, orange zest, olive oil sheen, crumbs on linen."),
("cocoa-almond-bark", "Cocoa Almond Bark", "Sweet Treats", "Dark chocolate bark with toasted almonds.", "2026-07-09", "20 mins", 10, "American",
 "Toast the almonds. Raw ones taste like wood.",
 ["8 oz dark chocolate", "1 cup almonds, toasted", "Flaky salt"],
 ["Melt chocolate. Stir in most almonds.", "Spread on parchment, top with remaining almonds and salt.", "Set in the fridge."],
 "Broken shards of cocoa almond bark, toasted almonds, flaky salt, glossy chocolate, photoreal."),
("roasted-pear-compote", "Roasted Pear Compote", "Sweet Treats", "Pears roasted with vanilla until they slump.", "2026-06-14", "40 mins", 4, "French-inspired",
 "Use pears that are almost too soft. Hard ones never give up.",
 ["4 pears, halved", "1 vanilla bean or 1 tsp extract", "2 tbsp sugar", "Butter"],
 ["Dot pears with butter and sugar, vanilla.", "Roast 375°F 30 minutes until collapsed.", "Spoon the juices over."],
 "Roasted pear halves in a dish, caramel juices, vanilla, collapsed fruit, photoreal dessert."),
("sesame-honey-cookies", "Sesame Honey Cookies", "Sweet Treats", "Chewy cookies heavy on sesame and honey.", "2026-05-12", "30 mins", 12, "Levantine-inspired",
 "Pull them when the edges set and the middle looks wet.",
 ["1 cup tahini", "1/2 cup honey", "1 egg", "1/2 tsp baking soda", "Sesame seeds"],
 ["Mix tahini, honey, egg, soda.", "Scoop, roll in sesame.", "Bake 350°F 10 minutes."],
 "A plate of sesame honey cookies, cracked tops, sesame, honey gloss, crumbs, photoreal."),
("coconut-rice-pudding", "Coconut Rice Pudding", "Sweet Treats", "Rice simmered in coconut milk until it slumps.", "2026-04-04", "40 mins", 4, "Southeast Asian-inspired",
 "Low heat. If it sticks, you rushed it.",
 ["1/2 cup jasmine rice", "1 can coconut milk", "2 cups water", "3 tbsp sugar", "Salt", "Lime zest"],
 ["Simmer rice, coconut milk, water, sugar, salt 30 minutes, stirring.", "It should be loose; it thickens off heat.", "Lime zest."],
 "Bowls of coconut rice pudding, thick, lime zest, coconut milk sheen, photoreal."),
("espresso-affogato-oat", "Espresso Affogato Oat", "Sweet Treats", "Oat ice cream drowned in hot espresso.", "2026-03-16", "5 mins", 2, "Italian-inspired",
 "Hot espresso, cold scoop, eat immediately.",
 ["4 scoops oat ice cream", "2 shots espresso"],
 ["Scoop ice cream into cold bowls.", "Pour espresso over. Serve at once."],
 "Oat ice cream with hot espresso poured over, melting pool, crema, ceramic cup, photoreal affogato."),
]

def md(r):
    slug, title, cat, desc, date, prep, serv, cui, intro, ings, steps, _photo = r
    acc = ACCENTS[hash(slug) % len(ACCENTS)]
    ings_md = "\n".join(f"- {i}" for i in ings)
    steps_md = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    return f"""---
title: {json.dumps(title)}
category: {json.dumps(cat)}
description: {json.dumps(desc)}
pubDate: {date}
prepTime: {json.dumps(prep)}
servings: {serv}
cuisine: {json.dumps(cui)}
accent: "{acc}"
---

{intro}

## Ingredients

{ings_md}

## Instructions

{steps_md}
"""

def write_recipes():
    RECIPES.mkdir(parents=True, exist_ok=True)
    for r in DATA:
        (RECIPES / f"{r[0]}.md").write_text(md(r))
    print(f"wrote {len(DATA)} recipes")

HEADER = """Generate photoreal recipe photos with the image_gen tool. Call image_gen once per dish below (parallel is fine). Every call MUST use aspect_ratio "4:3". After each file is written, copy it to the exact public path. Do not put words, watermarks, logos, or captions on the food. No people. No illustration, no CGI look.

Shared look: commercial cookbook food photography, three-quarter 45-degree view, 85mm f/2.8, shallow depth of field, soft directional window light from camera-left, warm editorial color grade, real textures (oil sheen, steam, condensation, crumbs), bone linen and rustic ceramic, extremely appetizing.

"""

def write_batches(size=8):
    PROMPTS.mkdir(parents=True, exist_ok=True)
    n = 0
    for i in range(0, len(DATA), size):
        chunk = DATA[i:i + size]
        n += 1
        lines = [HEADER]
        for j, r in enumerate(chunk, 1):
            slug, title, *_rest, photo = r
            lines.append(f"{j}. Save as public/recipes/{slug}.jpg\n{photo} Photoreal, delicious.\n")
        lines.append("When all listed files exist at those paths, print the paths and stop.\n")
        path = PROMPTS / f"batch-{n:02d}.md"
        path.write_text("\n".join(lines))
        print(path, len(chunk))
    return n

if __name__ == "__main__":
    write_recipes()
    write_batches()
