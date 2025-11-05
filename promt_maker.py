import random
import json
from datetime import datetime

class AdvancedPromptGenerator:
    def __init__(self):
        self.setup_comprehensive_data()
        self.categories = {
            "1": "photography",
            "2": "dark_moody", 
            "3": "bright_happy",
            "4": "classic",
            "5": "modern",
            "6": "wealthy",
            "7": "vintage",
            "8": "sports",
            "9": "gaming",
            "10": "profile",
            "11": "mobile_bg",
            "12": "desktop_bg",
            "13": "pro_photography",
            "14": "criminal",
            "15": "poor"
        }
    
    def setup_comprehensive_data(self):
        self.photography_subjects = [
            "portrait of elderly person with weathered face", "child laughing genuinely", 
            "professional dancer in motion", "mountain range at golden hour", 
            "desert dunes at sunrise", "urban architecture at blue hour",
            "wildlife in natural habitat", "street photography in busy market",
            "macro shot of water droplets", "food photography in restaurant kitchen"
        ]

        self.dark_moody_elements = [
            "abandoned asylum hallway", "lonely figure in foggy forest", "dark alley with single light",
            "haunted mansion interior", "stormy ocean cliffs", "industrial ruins at dusk",
            "gothic cathedral crypt", "shadowy figure in rain", "cemetery at midnight",
            "broken doll in attic", "sinister carnival at night", "apocalyptic cityscape"
        ]

        self.bright_happy_elements = [
            "children playing in sunflower field", "colorful festival celebration", 
            "beach party at sunset", "rainbow over waterfall", "happy family picnic",
            "vibrant street market", "birthday celebration with balloons", 
            "spring cherry blossom garden", "ice cream shop with friends",
            "sunny day in amusement park", "wedding ceremony moment"
        ]

        self.classic_elements = [
            "renaissance painting style", "baroque architecture interior", 
            "classical sculpture gallery", "vintage library with leather books",
            "traditional tea ceremony", "opera performance moment",
            "ballroom dance in palace", "antique furniture collection",
            "historical reenactment", "classic car showroom"
        ]

        self.modern_elements = [
            "sleek minimalist apartment", "contemporary art installation",
            "futuristic city transportation", "smart home technology",
            "modern architecture details", "tech startup office space",
            "futuristic vehicle design", "minimalist fashion",
            "abstract digital art", "sustainable eco-building"
        ]

        self.wealthy_elements = [
            "luxury penthouse with city view", "superyacht on mediterranean",
            "private jet interior", "designer fashion showroom",
            "exotic car collection", "fine dining michelin star restaurant",
            "luxury resort infinity pool", "high-end jewelry collection",
            "private art gallery", "executive office with skyline view"
        ]

        self.vintage_elements = [
            "1920s jazz club", "1950s diner interior", "vintage photography studio",
            "old pharmacy with antique bottles", "retro gaming arcade",
            "classic film noir scene", "vintage travel posters",
            "historical documentary style", "old workshop with tools",
            "vintage clothing store"
        ]

        self.sports_elements = [
            "basketball game final moment", "soccer penalty kick",
            "extreme sports action", "olympic athlete victory",
            "boxing match intensity", "surfing massive wave",
            "rock climbing summit", "marathon finish line",
            "winter sports competition", "team celebration moment"
        ]

        self.gaming_elements = [
            "cyberpunk cityscape", "fantasy RPG battlefield",
            "esports tournament arena", "retro gaming nostalgia",
            "VR gaming experience", "game character design",
            "gaming setup battlestation", "MMORPG world landscape",
            "strategy game overview", "game development studio"
        ]

        self.profile_elements = [
            "professional headshot", "creative self-portrait",
            "casual social media photo", "artistic avatar",
            "business profile image", "influencer style portrait",
            "character concept art", "minimalist profile icon",
            "thematic profile photo", "expression portrait"
        ]

        self.mobile_bg_elements = [
            "abstract liquid art", "minimalist geometric patterns",
            "nature landscape vertical", "cosmic space scene",
            "color gradient smooth", "textured background",
            "architectural details", "fantasy art vertical",
            "quote over background", "pattern repetition"
        ]

        self.desktop_bg_elements = [
            "epic landscape panorama", "digital art masterpiece",
            "cosmic universe wide", "city skyline wide",
            "fantasy world map", "abstract wide pattern",
            "minimalist wide design", "conceptual art wide",
            "nature wide panorama", "tech wide background"
        ]

        self.pro_photography_elements = [
            "commercial product photography", "fashion editorial shoot",
            "architectural masterpiece", "wildlife documentary",
            "wedding photography moment", "food commercial shoot",
            "corporate event coverage", "travel magazine spread",
            "portfolio quality image", "award-winning photo concept"
        ]

        self.criminal_elements = [
            "film noir detective scene", "heist planning moment",
            "undercover operation", "courtroom drama",
            "prison break tension", "gangster era speakeasy",
            "cybercrime hacker scene", "mystery thriller moment",
            "police investigation", "dramatic arrest scene"
        ]

        self.poor_elements = [
            "documentary street life", "abandoned industrial area",
            "refugee camp conditions", "urban poverty reality",
            "rural struggle scenes", "homeless shelter life",
            "working class daily life", "economic hardship story",
            "social documentary", "real life struggles"
        ]

        self.styles = [
            "cinematic", "photorealistic", "painterly", "minimalist",
            "surreal", "abstract", "conceptual", "documentary",
            "fine art", "editorial", "commercial", "fantasy",
            "sci-fi", "realism", "impressionism", "expressionism"
        ]
        
        self.techniques = [
            "dramatic lighting", "shallow depth of field", "high contrast",
            "soft lighting", "hard shadows", "vibrant colors",
            "muted tones", "black and white", "sepia tone",
            "HDR effect", "motion blur", "sharp focus"
        ]
        
        self.qualities = [
            "ultra detailed", "high resolution", "professional grade",
            "award winning", "masterpiece", "trending on artstation",
            "unreal engine render", "octane render", "4K quality",
            "photorealistic", "cinematic quality"
        ]

    def get_user_input(self):
        """Get user input for number of prompts and category"""
        print("🎨 Professional Prompt Generator")
        print("=" * 50)

        print("\nAvailable Categories:")
        print("1  - Photography")
        print("2  - Dark & Moody") 
        print("3  - Bright & Happy")
        print("4  - Classic")
        print("5  - Modern")
        print("6  - Wealthy")
        print("7  - Vintage")
        print("8  - Sports")
        print("9  - Gaming")
        print("10 - Profile Pictures")
        print("11 - Mobile Backgrounds")
        print("12 - Desktop Backgrounds")
        print("13 - Professional Photography")
        print("14 - Criminal (Dramatic/Fictional)")
        print("15 - Poor (Documentary Style)")

        while True:
            try:
                category_choice = input("\nSelect category (1-15): ").strip()
                if category_choice in self.categories:
                    break
                else:
                    print("❌ Please enter a number between 1 and 15")
            except:
                print("❌ Invalid input. Please try again.")

        while True:
            try:
                num_prompts = int(input("How many prompts to generate? (1-50): "))
                if 1 <= num_prompts <= 50:
                    break
                else:
                    print("❌ Please enter a number between 1 and 50")
            except:
                print("❌ Invalid input. Please enter a number.")
        
        return category_choice, num_prompts

    def generate_prompt(self, category_key):
        """Generate a prompt for the specified category"""
        category = self.categories[category_key]

        if category == "photography":
            base = random.choice(self.photography_subjects)
        elif category == "dark_moody":
            base = random.choice(self.dark_moody_elements)
        elif category == "bright_happy":
            base = random.choice(self.bright_happy_elements)
        elif category == "classic":
            base = random.choice(self.classic_elements)
        elif category == "modern":
            base = random.choice(self.modern_elements)
        elif category == "wealthy":
            base = random.choice(self.wealthy_elements)
        elif category == "vintage":
            base = random.choice(self.vintage_elements)
        elif category == "sports":
            base = random.choice(self.sports_elements)
        elif category == "gaming":
            base = random.choice(self.gaming_elements)
        elif category == "profile":
            base = random.choice(self.profile_elements)
        elif category == "mobile_bg":
            base = random.choice(self.mobile_bg_elements)
        elif category == "desktop_bg":
            base = random.choice(self.desktop_bg_elements)
        elif category == "pro_photography":
            base = random.choice(self.pro_photography_elements)
        elif category == "criminal":
            base = random.choice(self.criminal_elements)
        elif category == "poor":
            base = random.choice(self.poor_elements)

        style = random.choice(self.styles)
        technique = random.choice(self.techniques)
        quality = random.choice(self.qualities)

        prompt_parts = [base, f"{style} style", technique, quality]

        if random.random() < 0.6:
            prompt_parts.append(self.get_additional_detail(category))

        random.shuffle(prompt_parts)
        final_prompt = ", ".join(prompt_parts)
        
        return final_prompt

    def get_additional_detail(self, category):
        """Get additional details specific to each category"""
        details = {
            "photography": ["natural lighting", "studio quality", "professional composition"],
            "dark_moody": ["ominous atmosphere", "mysterious vibe", "dramatic shadows"],
            "bright_happy": ["vibrant colors", "happy atmosphere", "positive energy"],
            "classic": ["timeless beauty", "traditional elements", "historical accuracy"],
            "modern": ["contemporary design", "futuristic elements", "clean lines"],
            "wealthy": ["luxurious details", "high-end quality", "exclusive setting"],
            "vintage": ["aged texture", "retro aesthetic", "nostalgic feeling"],
            "sports": ["dynamic action", "competitive spirit", "athletic performance"],
            "gaming": ["digital art", "game aesthetics", "interactive elements"],
            "profile": ["personal expression", "social media ready", "identity representation"],
            "mobile_bg": ["vertical composition", "phone optimized", "lock screen ready"],
            "desktop_bg": ["wide format", "desktop optimized", "wallpaper ready"],
            "pro_photography": ["professional grade", "commercial quality", "portfolio level"],
            "criminal": ["dramatic tension", "storytelling moment", "suspenseful atmosphere"],
            "poor": ["raw emotion", "social commentary", "realistic depiction"]
        }
        
        return random.choice(details.get(category, ["high quality", "detailed", "professional"]))

    def generate_multiple_prompts(self, category_key, count):
        """Generate multiple prompts for the specified category"""
        prompts = []
        for i in range(count):
            prompt_text = self.generate_prompt(category_key)
            prompts.append({
                "id": i + 1,
                "prompt": prompt_text,
                "category": self.categories[category_key],
                "words": len(prompt_text.split())
            })
        return prompts

    def display_prompts(self, prompts, category_name):
        """Display generated prompts in a nice format"""
        print(f"\n🎨 Generated {len(prompts)} {category_name} Prompts:")
        print("=" * 60)
        
        for prompt_data in prompts:
            print(f"\n#{prompt_data['id']}:")
            print(f"📝 {prompt_data['prompt']}")
            print(f"📊 Words: {prompt_data['words']}")
            print("-" * 50)

    def save_to_file(self, prompts, category_name):
        """Save prompts to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{category_name}_prompts_{timestamp}.json"
        
        data = {
            "metadata": {
                "category": category_name,
                "count": len(prompts),
                "generated_at": datetime.now().isoformat()
            },
            "prompts": prompts
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filename

def main():
    generator = AdvancedPromptGenerator()

    category_choice, num_prompts = generator.get_user_input()
    category_name = generator.categories[category_choice].replace('_', ' ').title()

    print(f"\n🔄 Generating {num_prompts} {category_name} prompts...")
    prompts = generator.generate_multiple_prompts(category_choice, num_prompts)

    generator.display_prompts(prompts, category_name)

    save_choice = input("\n💾 Save these prompts to a file? (y/n): ").lower().strip()
    if save_choice in ['y', 'yes']:
        filename = generator.save_to_file(prompts, category_name)
        print(f"✅ Prompts saved to: {filename}")

    total_words = sum(p['words'] for p in prompts)
    avg_words = total_words / len(prompts)
    print(f"\n📊 Statistics:")
    print(f"   Total prompts: {len(prompts)}")
    print(f"   Average length: {avg_words:.1f} words")
    print(f"   Total words: {total_words}")

    again = input("\n🔄 Generate more prompts? (y/n): ").lower().strip()
    if again in ['y', 'yes']:
        main()
    else:
        print("👋 Thank you for using the Prompt Generator!")

if __name__ == "__main__":
    main()