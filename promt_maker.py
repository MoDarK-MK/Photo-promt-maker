import random
import json
import os
from datetime import datetime

class UltimatePromptMaster:
    def __init__(self):
        self.setup_comprehensive_data()
        self.setup_categories()
    
    def setup_categories(self):
        self.categories = {
            "1": "photography", "2": "dark_moody", "3": "bright_happy", 
            "4": "classic", "5": "modern", "6": "wealthy", "7": "vintage", 
            "8": "sports", "9": "gaming", "10": "profile", "11": "mobile_bg", 
            "12": "desktop_bg", "13": "pro_photography", "14": "criminal", 
            "15": "poor", "16": "fantasy", "17": "sci_fi", "18": "horror", 
            "19": "romantic", "20": "adventure", "21": "mystical", "22": "cyberpunk", 
            "23": "steampunk", "24": "abstract", "25": "nature", "26": "urban", 
            "27": "futuristic", "28": "historical", "29": "apocalyptic", 
            "30": "minimalist", "31": "anime", "32": "comic", "33": "cartoon", 
            "34": "realistic", "35": "surreal", "36": "conceptual", "37": "emotional", 
            "38": "action", "39": "dramatic", "40": "peaceful", "41": "chaotic", 
            "42": "orderly", "43": "magical", "44": "technological", "45": "organic"
        }

    def setup_comprehensive_data(self):
        self.scene_elements = {
            "photography": [
                "professional portrait session", "landscape photography", 
                "urban exploration", "wildlife photography", "macro photography",
                "street photography", "architectural photography", "food photography"
            ],
            "dark_moody": [
                "abandoned asylum", "foggy forest", "rainy alley", 
                "gothic cathedral", "industrial ruins", "cemetery at midnight"
            ],
            "fantasy": [
                "dragon flying over castle", "elf archer in forest", 
                "wizard casting spell", "magical kingdom", "ancient ruins"
            ],
            "sci_fi": [
                "spaceship interior", "alien planet", "future city",
                "cyborg enhancements", "space station"
            ]
        }

        self.core_elements = {
            "subjects": [
                "portrait of elderly person", "child laughing", "professional dancer",
                "mountain range", "desert dunes", "urban architecture", 
                "wildlife in habitat", "street market", "water droplets"
            ],
            "actions": [
                "casting dramatic shadows", "creating soft glow", "enhancing textures",
                "revealing intricate details", "capturing fleeting moments",
                "emphasizing natural beauty", "creating depth and dimension"
            ],
            "qualities": [
                "with incredible detail", "in perfect composition", "with balanced lighting",
                "showing realistic textures", "with vibrant colors", "in dramatic atmosphere",
                "with professional quality", "exhibiting masterful technique"
            ]
        }

        self.style_modifiers = {
            "lighting": [
                "cinematic lighting", "dramatic shadows", "soft glow", 
                "natural light", "studio lighting", "moody lighting"
            ],
            "composition": [
                "rule of thirds", "symmetrical balance", "leading lines",
                "negative space", "layered depth", "dynamic angles"
            ],
            "mood": [
                "epic and grand", "intimate and personal", "mysterious and enigmatic",
                "joyful and vibrant", "peaceful and serene", "dramatic and intense"
            ]
        }

        self.technical_terms = {
            "camera": [
                "medium format", "full frame DSLR", "mirrorless camera",
                "vintage film", "cinema camera", "drone photography"
            ],
            "lens": [
                "wide angle", "prime lens", "telephoto", "macro lens",
                "tilt-shift", "anamorphic"
            ],
            "settings": [
                "shallow depth of field", "long exposure", "HDR technique",
                "focus stacking", "high speed sync", "time-lapse"
            ]
        }

        self.artistic_descriptors = [
            "hyperrealistic", "photorealistic", "cinematic", "painterly",
            "impressionistic", "surreal", "abstract", "minimalist",
            "maximalist", "conceptual", "fine art", "editorial"
        ]

        # کیفیت تصویر و رزولوشن
        self.image_quality = {
            "resolution": {
                "low": ["low resolution", "basic quality", "standard definition"],
                "medium": ["medium resolution", "good quality", "HD quality"],
                "high": ["high resolution", "excellent quality", "full HD"],
                "ultra": ["ultra high resolution", "4K quality", "UHD"],
                "extreme": ["8K resolution", "extreme detail", "maximum quality"]
            },
            "detail_level": {
                "basic": ["basic details", "clean image", "clear rendering"],
                "standard": ["good details", "sharp image", "clean rendering"],
                "detailed": ["high detail", "very sharp", "crisp details"],
                "extreme": ["extreme detail", "ultra sharp", "micro details"],
                "hyper": ["hyper detailed", "maximum sharpness", "perfect clarity"]
            },
            "render_quality": {
                "fast": ["fast render", "quick processing", "efficient rendering"],
                "balanced": ["balanced render", "good performance", "smooth rendering"],
                "quality": ["quality render", "fine processing", "clean output"],
                "premium": ["premium render", "excellent processing", "master rendering"],
                "ultimate": ["ultimate render", "best quality", "perfect rendering"]
            },
            "engine_specific": {
                "basic": ["clean output", "good rendering", "standard quality"],
                "advanced": ["octane render", "v-ray quality", "arnold renderer"],
                "premium": ["unreal engine 5", "cycles render", "luxcore render"],
                "ultimate": ["masterpiece rendering", "studio quality", "Hollywood VFX quality"]
            }
        }

        self.detail_levels = {
            "minimal": [1, 2],
            "light": [3, 5],
            "moderate": [6, 10],
            "detailed": [11, 20],
            "comprehensive": [21, 35],
            "extreme": [36, 50]
        }

        self.quality_presets = {
            "1": {"name": "Low Quality", "resolution": "low", "detail": "basic", "render": "fast", "engine": "basic"},
            "2": {"name": "Medium Quality", "resolution": "medium", "detail": "standard", "render": "balanced", "engine": "basic"},
            "3": {"name": "High Quality", "resolution": "high", "detail": "detailed", "render": "quality", "engine": "advanced"},
            "4": {"name": "Ultra Quality", "resolution": "ultra", "detail": "extreme", "render": "premium", "engine": "premium"},
            "5": {"name": "Extreme Quality", "resolution": "extreme", "detail": "hyper", "render": "ultimate", "engine": "ultimate"}
        }

    def get_user_input(self):
        print("🎨 SMART PROMPT GENERATOR WITH QUALITY CONTROL")
        print("=" * 60)
        
        print("\nAVAILABLE CATEGORIES:")
        categories_display = []
        for key, value in self.categories.items():
            category_name = value.replace('_', ' ').title()
            categories_display.append(f"{key:>2} - {category_name}")
        
        for i in range(0, len(categories_display), 3):
            print(" | ".join(categories_display[i:i+3]))
        
        while True:
            try:
                category_choice = input("\nSelect category (1-45): ").strip()
                if category_choice in self.categories:
                    break
                print("Invalid choice. Please enter a number between 1 and 45")
            except:
                print("Invalid input. Please try again.")
        
        while True:
            try:
                num_prompts = int(input("How many prompts to generate? (1-1000): "))
                if 1 <= num_prompts <= 1000:
                    break
                print("Please enter a number between 1 and 1000")
            except:
                print("Invalid input. Please enter a number.")

        print("\n📝 WORD COUNT OPTIONS:")
        print("minimal (1-2) | light (3-5) | moderate (6-10) | detailed (11-20) | comprehensive (21-35) | extreme (36-50)")
        
        while True:
            try:
                word_choice = input("Choose word count level or enter exact number (1-50): ").strip().lower()
                
                if word_choice in self.detail_levels:
                    min_words, max_words = self.detail_levels[word_choice]
                    break
                elif word_choice.isdigit():
                    word_count = int(word_choice)
                    if 1 <= word_count <= 50:
                        min_words = max_words = word_count
                        break
                    else:
                        print("Please enter a number between 1 and 50")
                else:
                    print("Invalid choice. Please enter a level or number between 1 and 50")
            except:
                print("Invalid input. Please try again.")

        print("\n🎯 IMAGE QUALITY PRESETS:")
        print("1 - Low Quality (fast rendering)")
        print("2 - Medium Quality (balanced)")
        print("3 - High Quality (recommended)")
        print("4 - Ultra Quality (premium)")
        print("5 - Extreme Quality (maximum detail)")
        
        while True:
            try:
                quality_choice = input("Select quality preset (1-5): ").strip()
                if quality_choice in self.quality_presets:
                    quality_preset = self.quality_presets[quality_choice]
                    break
                else:
                    print("Please enter a number between 1 and 5")
            except:
                print("Invalid input. Please try again.")
        
        return category_choice, num_prompts, min_words, max_words, quality_preset

    def generate_quality_terms(self, quality_preset, available_words):
        """تولید عبارت‌های کیفیت تصویر بر اساس پریست و تعداد کلمات موجود"""
        quality_terms = []
        
        # انتخاب عبارات بر اساس پریست کیفیت
        resolution = random.choice(self.image_quality["resolution"][quality_preset["resolution"]])
        detail = random.choice(self.image_quality["detail_level"][quality_preset["detail"]])
        render = random.choice(self.image_quality["render_quality"][quality_preset["render"]])
        engine = random.choice(self.image_quality["engine_specific"][quality_preset["engine"]])
        
        # ترکیب عبارات بر اساس تعداد کلمات موجود
        if available_words >= 8:
            # حالت کامل
            quality_terms = [resolution, detail, render, engine]
        elif available_words >= 6:
            # حالت متوسط
            quality_terms = [resolution, detail, render]
        elif available_words >= 4:
            # حالت کوتاه
            quality_terms = [resolution, detail]
        elif available_words >= 2:
            # حالت بسیار کوتاه
            quality_terms = [resolution]
        else:
            # حداقل کیفیت
            quality_terms = ["high quality"]
        
        return quality_terms

    def generate_smart_prompt(self, category_key, min_words, max_words, quality_preset):
        category = self.categories[category_key]
        
        target_words = random.randint(min_words, max_words)
        
        prompt_parts = []
        current_words = 0
        
        # محاسبه فضای مورد نیاز برای عبارات کیفیت
        quality_words_reserve = min(8, max(2, target_words // 4))
        main_content_words = target_words - quality_words_reserve
        
        # تولید محتوای اصلی
        base_category = category if category in self.scene_elements else "photography"
        scene = random.choice(self.scene_elements.get(base_category, self.scene_elements["photography"]))
        prompt_parts.append(scene)
        current_words += len(scene.split())
        
        if main_content_words > 3:
            subject = random.choice(self.core_elements["subjects"])
            prompt_parts.append(subject)
            current_words += len(subject.split())
        
        if main_content_words > 6:
            style = random.choice(self.artistic_descriptors)
            prompt_parts.append(style + " style")
            current_words += 2
        
        if main_content_words > 10:
            lighting = random.choice(self.style_modifiers["lighting"])
            prompt_parts.append(lighting)
            current_words += len(lighting.split())
        
        if main_content_words > 15:
            composition = random.choice(self.style_modifiers["composition"])
            prompt_parts.append(composition)
            current_words += len(composition.split())
            
            mood = random.choice(self.style_modifiers["mood"])
            prompt_parts.append(mood)
            current_words += len(mood.split())
        
        # اضافه کردن عبارات کیفیت
        available_quality_words = target_words - current_words
        if available_quality_words > 0:
            quality_terms = self.generate_quality_terms(quality_preset, available_quality_words)
            prompt_parts.extend(quality_terms)
            current_words += sum(len(term.split()) for term in quality_terms)
        
        # تنظیم نهایی تعداد کلمات
        while current_words < target_words and len(prompt_parts) < 15:
            available_space = target_words - current_words
            
            if available_space >= 3:
                additional_elements = [
                    random.choice(self.style_modifiers["lighting"]),
                    random.choice(self.style_modifiers["composition"]),
                    random.choice(self.core_elements["qualities"]),
                    random.choice(self.technical_terms["settings"])
                ]
                new_element = random.choice(additional_elements)
                if new_element not in prompt_parts:
                    prompt_parts.append(new_element)
                    current_words += len(new_element.split())
            else:
                short_modifiers = ["detailed", "sharp", "vibrant", "dramatic", "soft"]
                modifier = random.choice(short_modifiers)
                if modifier not in ' '.join(prompt_parts):
                    prompt_parts.append(modifier)
                    current_words += 1
        
        random.shuffle(prompt_parts)
        
        final_prompt = ", ".join(prompt_parts)
        actual_words = len(final_prompt.split())
        
        # بهینه‌سازی نهایی
        if actual_words < min_words:
            while actual_words < min_words:
                short_boosters = ["high quality", "professional", "masterpiece", "award winning"]
                booster = random.choice(short_boosters)
                if booster not in final_prompt:
                    final_prompt += ", " + booster
                    actual_words += 2
        
        elif actual_words > max_words:
            words = final_prompt.split()
            final_prompt = " ".join(words[:max_words])
            actual_words = max_words
        
        return final_prompt, actual_words, target_words

    def generate_multiple_prompts(self, category_key, count, min_words, max_words, quality_preset):
        prompts = []
        for i in range(count):
            prompt_text, actual_words, target_words = self.generate_smart_prompt(
                category_key, min_words, max_words, quality_preset
            )
            
            prompts.append({
                "id": i + 1,
                "prompt": prompt_text,
                "category": self.categories[category_key],
                "actual_words": actual_words,
                "target_words": target_words,
                "characters": len(prompt_text),
                "quality_preset": quality_preset["name"],
                "efficiency": "perfect" if actual_words == target_words else "good" if abs(actual_words - target_words) <= 2 else "adjusted"
            })
        return prompts

    def display_prompts(self, prompts, category_name, min_words, max_words, quality_preset):
        quality_name = quality_preset["name"]
        print(f"\n🎨 GENERATED {len(prompts)} {category_name.upper()} PROMPTS")
        print(f"🎯 QUALITY: {quality_name} | WORDS: {min_words}-{max_words}")
        print("=" * 80)
        
        for prompt_data in prompts:
            print(f"\n#{prompt_data['id']:03d} [{prompt_data['efficiency'].upper()} | {prompt_data['quality_preset']}]:")
            print(f"📝 {prompt_data['prompt']}")
            print(f"📊 Words: {prompt_data['actual_words']} (target: {prompt_data['target_words']}) | Chars: {prompt_data['characters']}")
            print("-" * 80)

    def save_to_file(self, prompts, category_name, min_words, max_words, quality_preset):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        quality_slug = quality_preset["name"].replace(" ", "_").lower()
        filename = f"QUALITY_{quality_slug}_{category_name}_{min_words}-{max_words}words_{timestamp}.json"
        
        data = {
            "metadata": {
                "category": category_name,
                "count": len(prompts),
                "word_range": f"{min_words}-{max_words}",
                "quality_preset": quality_preset,
                "generated_at": datetime.now().isoformat(),
                "version": "quality_1.0",
                "total_words": sum(p['actual_words'] for p in prompts),
                "average_words": sum(p['actual_words'] for p in prompts) / len(prompts),
                "perfect_matches": sum(1 for p in prompts if p['efficiency'] == 'perfect')
            },
            "prompts": prompts
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filename

    def show_statistics(self, prompts, min_words, max_words, quality_preset):
        total_words = sum(p['actual_words'] for p in prompts)
        total_chars = sum(p['characters'] for p in prompts)
        avg_words = total_words / len(prompts)
        avg_chars = total_chars / len(prompts)
        
        perfect = sum(1 for p in prompts if p['efficiency'] == 'perfect')
        good = sum(1 for p in prompts if p['efficiency'] == 'good')
        adjusted = sum(1 for p in prompts if p['efficiency'] == 'adjusted')
        
        print(f"\n📊 QUALITY GENERATION STATISTICS:")
        print(f"   Total prompts: {len(prompts)}")
        print(f"   Quality preset: {quality_preset['name']}")
        print(f"   Target word range: {min_words}-{max_words}")
        print(f"   Perfect word matches: {perfect}")
        print(f"   Good matches (±2 words): {good}")
        print(f"   Adjusted prompts: {adjusted}")
        print(f"   Average length: {avg_words:.1f} words")
        print(f"   Average characters: {avg_chars:.1f}")
        print(f"   Total words generated: {total_words}")
        print(f"   Min words: {min(p['actual_words'] for p in prompts)}")
        print(f"   Max words: {max(p['actual_words'] for p in prompts)}")
        
        # نمایش جزئیات کیفیت
        print(f"\n🎯 QUALITY SETTINGS APPLIED:")
        print(f"   Resolution: {quality_preset['resolution']}")
        print(f"   Detail level: {quality_preset['detail']}")
        print(f"   Render quality: {quality_preset['render']}")
        print(f"   Engine: {quality_preset['engine']}")

def main():
    generator = UltimatePromptMaster()
    
    while True:
        category_choice, num_prompts, min_words, max_words, quality_preset = generator.get_user_input()
        category_name = generator.categories[category_choice].replace('_', ' ').title()
        
        print(f"\n🔄 Generating {num_prompts} {quality_preset['name']} {category_name} prompts ({min_words}-{max_words} words)...")
        
        prompts = generator.generate_multiple_prompts(category_choice, num_prompts, min_words, max_words, quality_preset)
        
        generator.display_prompts(prompts, category_name, min_words, max_words, quality_preset)
        generator.show_statistics(prompts, min_words, max_words, quality_preset)
        
        save_choice = input("\n💾 Save these quality-controlled prompts to a file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes']:
            filename = generator.save_to_file(prompts, category_name, min_words, max_words, quality_preset)
            print(f"✅ Quality prompts saved to: {filename}")
        
        again = input("\n🔄 Generate more quality prompts? (y/n): ").lower().strip()
        if again not in ['y', 'yes']:
            print("👋 Thank you for using the Quality-Controlled Prompt Generator!")
            break

if __name__ == "__main__":
    main()