import random
import json
import os
from datetime import datetime

class UltimatePromptGenerator:
    def __init__(self):
        self.setup_master_data()
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

    def setup_master_data(self):
        self.master_elements = {
            "photography": [
                "professional portrait with perfect lighting", "landscape at golden hour", 
                "urban exploration photography", "wildlife in natural habitat", 
                "macro photography with incredible detail", "street photography candid moment",
                "architectural photography with strong lines", "food photography styled perfectly",
                "sports action frozen in time", "fashion editorial with model"
            ],
            "dark_moody": [
                "abandoned asylum with haunting atmosphere", "foggy forest with mysterious figure",
                "rainy alley with single street lamp", "gothic cathedral interior shadows",
                "industrial decay with dramatic lighting", "cemetery at midnight with full moon",
                "broken doll in dusty attic", "sinister carnival after hours",
                "apocalyptic cityscape with ruins", "underground tunnel with dripping water"
            ],
            "bright_happy": [
                "children laughing in sunflower field", "beach party at sunset with friends",
                "colorful festival with dancing people", "rainbow over waterfall in jungle",
                "birthday celebration with balloons and cake", "ice cream shop with happy customers",
                "spring garden full of blooming flowers", "amusement park with excited visitors",
                "family picnic in sunny park", "wedding ceremony with joyful moments"
            ],
            "classic": [
                "renaissance painting recreation", "baroque palace grand hall",
                "classical sculpture gallery marble", "vintage library leather books",
                "traditional Japanese tea ceremony", "opera performance dramatic moment",
                "ballroom dance in historic palace", "antique furniture collection",
                "historical battle reenactment", "classic car showroom polished"
            ],
            "modern": [
                "minimalist apartment clean lines", "contemporary art installation",
                "futuristic transportation design", "smart home technology integration",
                "modern architecture glass steel", "tech startup open office",
                "sleek vehicle aerodynamic design", "minimalist fashion runway",
                "abstract digital art patterns", "sustainable building eco-friendly"
            ],
            "wealthy": [
                "luxury penthouse city skyline", "superyacht mediterranean cruise",
                "private jet interior luxury", "designer fashion boutique",
                "exotic car collection garage", "michelin star restaurant dining",
                "private island resort paradise", "high-end jewelry sparkling",
                "exclusive art gallery opening", "corporate executive office view"
            ],
            "vintage": [
                "1920s jazz club speakeasy", "1950s diner retro interior",
                "vintage photography studio setup", "old pharmacy antique bottles",
                "retro gaming arcade machines", "film noir detective office",
                "vintage travel poster art", "historical documentary style",
                "old workshop traditional tools", "vintage clothing store fashion"
            ],
            "sports": [
                "basketball game final buzzer", "soccer penalty kick tension",
                "extreme sports action shot", "olympic athlete victory moment",
                "boxing match intense exchange", "surfing massive wave barrel",
                "rock climbing summit achievement", "marathon finish line effort",
                "winter sports ski jump", "team championship celebration"
            ],
            "gaming": [
                "cyberpunk city neon lights", "fantasy RPG epic battle",
                "esports arena packed crowd", "retro gaming nostalgia pixels",
                "VR gaming immersive experience", "game character design concept",
                "gaming setup ultimate battlestation", "MMORPG world landscape",
                "strategy game overview map", "game development studio creative"
            ],
            "profile": [
                "professional headshot corporate", "creative self-portrait artistic",
                "social media influencer style", "artistic avatar digital",
                "business profile professional", "character concept portrait",
                "minimalist icon simple", "thematic profile cohesive",
                "expression portrait emotional", "gaming profile competitive"
            ],
            "mobile_bg": [
                "abstract liquid art colors", "minimalist geometric patterns clean",
                "nature landscape vertical format", "cosmic space nebula stars",
                "color gradient smooth transition", "textured background tactile",
                "architectural details lines", "fantasy art vertical scene",
                "inspirational quote typography", "pattern repetition hypnotic"
            ],
            "desktop_bg": [
                "epic landscape wide panorama", "digital art masterpiece detailed",
                "cosmic universe expansive", "city skyline wide angle",
                "fantasy world map illustrated", "abstract wide pattern flowing",
                "minimalist wide design clean", "conceptual art thought provoking",
                "nature wide panorama breathtaking", "tech wide background futuristic"
            ],
            "pro_photography": [
                "commercial product studio shot", "fashion editorial high fashion",
                "architectural masterpiece design", "wildlife documentary natural",
                "wedding photography emotional", "food commercial appetizing",
                "corporate event professional", "travel magazine exotic",
                "portfolio quality exceptional", "award-winning photo unique"
            ],
            "criminal": [
                "film noir detective shadowy", "heist planning intricate",
                "undercover operation tense", "courtroom drama intense",
                "prison break dramatic", "gangster era powerful",
                "cybercrime hacker mysterious", "mystery thriller suspenseful",
                "police investigation detailed", "dramatic arrest action"
            ],
            "poor": [
                "documentary street raw", "abandoned industrial decaying",
                "refugee camp reality", "urban poverty stark",
                "rural struggle authentic", "homeless shelter humanity",
                "working class daily", "economic hardship truth",
                "social documentary powerful", "real life struggles genuine"
            ],
            "fantasy": [
                "dragon flying over castle", "elf archer in enchanted forest",
                "wizard casting powerful spell", "mythical creature ancient",
                "magical kingdom floating", "epic quest beginning",
                "fantasy battle massive", "enchanted waterfall mystical",
                "ancient ruins magical", "mythical beast legendary"
            ],
            "sci_fi": [
                "spaceship interior futuristic", "alien planet landscape strange",
                "future city advanced technology", "cyborg enhancements detailed",
                "space station orbiting", "time travel device complex",
                "robot society advanced", "holographic interface glowing",
                "genetic engineering lab", "interstellar travel gateway"
            ],
            "horror": [
                "haunted house terrifying", "psychological horror mind bending",
                "supernatural entity ominous", "body horror disturbing",
                "slasher film intense", "ghost story chilling",
                "lovecraftian horror cosmic", "zombie apocalypse survival",
                "demonic possession dramatic", "creature feature monstrous"
            ],
            "romantic": [
                "couple sunset embrace", "romantic dinner intimate",
                "love story beginning", "wedding proposal emotional",
                "romantic getaway scenic", "first kiss magical",
                "eternal love symbolic", "romantic gesture sweet",
                "heartfelt moment genuine", "romantic comedy lively"
            ],
            "adventure": [
                "mountain climbing epic", "jungle exploration mysterious",
                "desert expedition vast", "deep sea diving unknown",
                "space exploration cosmic", "treasure hunt exciting",
                "wilderness survival challenging", "road trip freedom",
                "ancient discovery groundbreaking", "expedition team united"
            ],
            "mystical": [
                "magic portal glowing", "ancient prophecy unfolding",
                "mystical energy flowing", "enchanted forest alive",
                "magical ritual ancient", "spiritual journey profound",
                "mystic sage wise", "magical artifact powerful",
                "vision quest transformative", "mystical realm otherworldly"
            ],
            "cyberpunk": [
                "neon-lit rainy streets", "cybernetic enhancements visible",
                "megacorporation dystopian", "hacker underground hideout",
                "future noir detective", "augmented reality overlay",
                "cybernetics lab advanced", "neon city vertical",
                "digital consciousness virtual", "tech rebellion underground"
            ],
            "steampunk": [
                "victorian era technology", "brass gears intricate",
                "steam-powered machinery", "airship flying majestic",
                "clockwork automaton detailed", "industrial revolution advanced",
                "retro-futuristic inventions", "cogwheel mechanism complex",
                "steam engine powerful", "alternate history creative"
            ],
            "abstract": [
                "geometric shapes complex", "color theory exploration",
                "form and space relationship", "texture patterns intricate",
                "optical illusion mind bending", "non-representational art",
                "emotional abstraction raw", "mathematical patterns precise",
                "organic forms flowing", "digital abstraction glitch"
            ],
            "nature": [
                "untouched wilderness pristine", "ecosystem diversity rich",
                "natural phenomena powerful", "wildlife behavior natural",
                "botanical details intricate", "geological formations ancient",
                "weather patterns dramatic", "seasonal changes beautiful",
                "natural cycles eternal", "environmental conservation important"
            ],
            "urban": [
                "city life dynamic", "urban architecture diverse",
                "street culture vibrant", "public spaces lively",
                "urban development ongoing", "city rhythms fast",
                "metropolitan diversity rich", "urban landscape layered",
                "city lights dazzling", "urban exploration revealing"
            ],
            "futuristic": [
                "advanced technology integrated", "future society evolved",
                "smart city efficient", "space colonization beginning",
                "AI integration seamless", "biotechnology revolutionary",
                "quantum computing powerful", "future transportation fast",
                "smart materials adaptive", "digital society connected"
            ],
            "historical": [
                "ancient civilization grand", "historical event significant",
                "period accurate recreation", "archaeological discovery important",
                "historical figure influential", "ancient artifacts precious",
                "historical battle decisive", "ancient knowledge preserved",
                "historical timeline visual", "cultural heritage rich"
            ],
            "apocalyptic": [
                "post-apocalyptic world barren", "survival scenario desperate",
                "world after catastrophe", "abandoned civilization remains",
                "environmental collapse aftermath", "nuclear winter bleak",
                "zombie wasteland dangerous", "alien invasion aftermath",
                "climate disaster impact", "dystopian society oppressive"
            ],
            "minimalist": [
                "essential elements only", "clean lines precise",
                "negative space balanced", "simplicity elegant",
                "monochromatic palette refined", "geometric purity perfect",
                "reduced composition focused", "essential beauty revealed",
                "minimal detail maximum impact", "clean aesthetic pleasing"
            ],
            "anime": [
                "anime style vibrant", "manga inspired dynamic",
                "character design kawaii", "anime landscape detailed",
                "mecha design complex", "shonen action intense",
                "shojo romance sweet", "isekai fantasy imaginative",
                "anime food delicious", "chibi style cute"
            ],
            "comic": [
                "comic book style bold", "graphic novel atmospheric",
                "superhero action powerful", "comic panel sequential",
                "speech bubble dialogue", "inking techniques varied",
                "color palette comic", "character design iconic",
                "action lines dynamic", "comic cover eye-catching"
            ],
            "cartoon": [
                "animation style lively", "character expression exaggerated",
                "cartoon physics fun", "animated world colorful",
                "cartoon network style", "disney animation quality",
                "looney tunes chaotic", "adventure time weird",
                "rick and morty sci-fi", "spongebob squarepants silly"
            ],
            "realistic": [
                "photorealistic detail incredible", "hyperrealism stunning",
                "texture perfect replication", "lighting natural accurate",
                "perspective correct precise", "material representation exact",
                "human expression genuine", "environment authentic believable",
                "still life perfect", "portrait lifelike"
            ],
            "surreal": [
                "dream logic bizarre", "reality distorted strange",
                "unconscious mind revealed", "fantastical elements unexpected",
                "metaphorical imagery deep", "psychological landscape internal",
                "impossible architecture mind-bending", "floating elements weightless",
                "scale manipulation disorienting", "surreal narrative mysterious"
            ],
            "conceptual": [
                "idea visualization abstract", "philosophical concept deep",
                "metaphor visual powerful", "intellectual exploration thoughtful",
                "conceptual art meaningful", "thought process visual",
                "abstract idea concrete", "mental model structural",
                "conceptual framework clear", "idea manifestation creative"
            ],
            "emotional": [
                "human emotion raw", "emotional journey transformative",
                "psychological depth profound", "emotional expression authentic",
                "inner conflict visible", "emotional landscape internal",
                "feeling atmosphere palpable", "emotional resonance strong",
                "vulnerability beautiful", "emotional truth powerful"
            ],
            "action": [
                "dynamic movement frozen", "energy explosion dramatic",
                "motion blur speed", "action sequence intense",
                "physical exertion visible", "combat moment decisive",
                "sports action peak", "chase scene thrilling",
                "explosion moment catastrophic", "action pose powerful"
            ],
            "dramatic": [
                "theatrical lighting dramatic", "emotional tension high",
                "storytelling moment pivotal", "confrontation scene intense",
                "climactic moment epic", "dramatic composition strong",
                "emotional stakes high", "character development visible",
                "narrative arc clear", "dramatic reveal surprising"
            ],
            "peaceful": [
                "tranquil scene serene", "calm atmosphere soothing",
                "peaceful moment quiet", "meditative state calm",
                "harmony visual balanced", "stillness beautiful",
                "relaxation atmosphere comfortable", "peaceful landscape inviting",
                "quiet contemplation thoughtful", "serene environment peaceful"
            ],
            "chaotic": [
                "organized chaos structured", "chaotic energy wild",
                "disorder beautiful", "chaotic composition dynamic",
                "energy explosion chaotic", "chaotic patterns intricate",
                "turmoil visual intense", "chaotic movement frenetic",
                "disarray artistic", "chaotic balance perfect"
            ],
            "orderly": [
                "perfect symmetry precise", "organized structure clean",
                "systematic arrangement logical", "order visual pleasing",
                "pattern repetition hypnotic", "geometric order perfect",
                "structured composition balanced", "mathematical precision exact",
                "organized chaos controlled", "system visualization clear"
            ],
            "magical": [
                "magic sparkle enchanting", "enchanted atmosphere mystical",
                "magical transformation amazing", "spell casting powerful",
                "magical creature fantastic", "enchanted object mysterious",
                "magical energy flowing", "wonderland fantasy",
                "magical realism blend", "supernatural elements magical"
            ],
            "technological": [
                "advanced machinery complex", "digital interface sleek",
                "technology integration seamless", "futuristic devices innovative",
                "circuit patterns intricate", "data visualization beautiful",
                "tech components detailed", "innovation visible",
                "digital transformation clear", "technological progress evident"
            ],
            "organic": [
                "natural forms flowing", "biological patterns intricate",
                "organic growth visible", "living structures complex",
                "natural materials authentic", "biological diversity rich",
                "organic shapes beautiful", "living systems interconnected",
                "natural processes ongoing", "organic texture tactile"
            ]
        }

        self.art_styles = [
            "hyperrealistic", "photorealistic", "cinematic", "painterly", "impressionistic",
            "expressionistic", "surreal", "abstract", "conceptual", "minimalist",
            "maximalist", "brutalist", "art deco", "art nouveau", "baroque",
            "renaissance", "romantic", "gothic", "byzantine", "modernist",
            "postmodern", "contemporary", "digital", "traditional", "mixed media",
            "collage", "vector", "pixel", "3D render", "claymation",
            "stop motion", "anime", "manga", "comic book", "graphic novel",
            "cartoon", "caricature", "carTOON", "illustration", "sketch",
            "watercolor", "oil painting", "acrylic", "pastel", "charcoal",
            "ink wash", "woodcut", "linocut", "etching", "lithograph"
        ]

        self.techniques = [
            "dramatic lighting", "chiaroscuro", "soft lighting", "hard lighting",
            "rim lighting", "backlighting", "side lighting", "top lighting",
            "bottom lighting", "natural lighting", "studio lighting", "ambient lighting",
            "mood lighting", "color grading", "high contrast", "low contrast",
            "saturated colors", "desaturated colors", "monochromatic", "complementary colors",
            "analogous colors", "warm colors", "cool colors", "pastel colors",
            "vibrant colors", "muted colors", "black and white", "sepia tone",
            "selective color", "color splash", "motion blur", "depth of field",
            "shallow focus", "deep focus", "tilt shift", "macro photography",
            "wide angle", "telephoto", "fisheye", "panoramic",
            "time lapse", "long exposure", "high speed", "slow motion",
            "multiple exposure", "HDR", "bokeh", "vignette",
            "film grain", "digital noise", "sharp focus", "soft focus",
            "rule of thirds", "golden ratio", "symmetrical composition", "asymmetrical composition",
            "leading lines", "framing", "negative space", "positive space",
            "texture mapping", "pattern repetition", "scale variation", "perspective distortion"
        ]

        self.qualities = [
            "ultra detailed", "high resolution", "8K", "4K",
            "professional grade", "masterpiece", "award winning", "trending on artstation",
            "unreal engine render", "octane render", "v-ray render", "arnold render",
            "cycles render", "eevee render", "photorealistic", "hyperrealistic",
            "cinematic quality", "studio quality", "commercial grade", "editorial quality",
            "fine art quality", "gallery quality", "museum quality", "exhibition quality",
            "print ready", "web optimized", "social media ready", "portfolio piece",
            "concept art quality", "illustration quality", "digital art", "traditional art",
            "mixed media", "collage art", "vector art", "pixel art",
            "3D art", "2D art", "animated", "static",
            "dynamic", "static", "energetic", "calm",
            "powerful", "subtle", "bold", "delicate",
            "intricate", "simple", "complex", "minimal",
            "maximal", "saturated", "desaturated", "vibrant",
            "muted", "bright", "dark", "contrasty",
            "flat", "dimensional", "textured", "smooth"
        ]

        self.moods = [
            "epic", "intimate", "dramatic", "subtle",
            "powerful", "delicate", "intense", "calm",
            "chaotic", "orderly", "harmonious", "discordant",
            "joyful", "sad", "angry", "peaceful",
            "anxious", "confident", "vulnerable", "strong",
            "mysterious", "clear", "ambiguous", "definite",
            "hopeful", "despairing", "optimistic", "pessimistic",
            "romantic", "platonic", "familial", "solitary",
            "social", "isolated", "connected", "disconnected",
            "natural", "artificial", "organic", "synthetic",
            "traditional", "modern", "futuristic", "historical",
            "timeless", "dated", "contemporary", "classic",
            "edgy", "mainstream", "alternative", "conventional",
            "rebellious", "conformist", "individual", "collective"
        ]

        self.perspectives = [
            "eye level", "low angle", "high angle", "bird's eye view",
            "worm's eye view", "dutch angle", "straight on", "profile view",
            "three-quarter view", "frontal view", "rear view", "side view",
            "aerial view", "ground level", "underwater", "microscopic",
            "telescopic", "wide shot", "medium shot", "close up",
            "extreme close up", "establishing shot", "master shot", "point of view",
            "over the shoulder", "two shot", "group shot", "canted angle",
            "zoom perspective", "dolly zoom", "tracking shot", "steadycam",
            "crane shot", "helicopter shot", "drone shot", "satellite view",
            "first person", "third person", "isometric", "forced perspective",
            "fisheye perspective", "wide angle perspective", "telephoto perspective", "macro perspective",
            "tilt shift perspective", "panoramic perspective", "360 degree view", "VR perspective",
            "AR perspective", "holographic projection", "x-ray vision", "thermal vision",
            "night vision", "ultraviolet vision", "infrared vision", "multispectral imaging"
        ]

    def get_user_input(self):
        print("🎨 ULTIMATE PROMPT GENERATOR")
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
                num_prompts = int(input("How many prompts to generate? (1-100): "))
                if 1 <= num_prompts <= 100:
                    break
                print("Please enter a number between 1 and 100")
            except:
                print("Invalid input. Please enter a number.")
        
        return category_choice, num_prompts

    def generate_prompt(self, category_key):
        category = self.categories[category_key]
        
        base_element = random.choice(self.master_elements.get(category, ["creative concept"]))
        
        components = []
        components.append(base_element)
        
        if random.random() < 0.8:
            components.append(random.choice(self.art_styles))
        
        if random.random() < 0.7:
            components.append(random.choice(self.techniques))
        
        if random.random() < 0.6:
            components.append(random.choice(self.moods))
        
        if random.random() < 0.5:
            components.append(random.choice(self.perspectives))
        
        if random.random() < 0.9:
            components.append(random.choice(self.qualities))
        
        if random.random() < 0.4:
            components.append(f"by {random.choice(['famous artist', 'renowned photographer', 'digital artist'])}")
        
        if random.random() < 0.3:
            components.append(f"inspired by {random.choice(['classic masterpiece', 'contemporary art', 'cultural movement'])}")
        
        random.shuffle(components)
        
        prompt = ", ".join(components)
        
        return prompt

    def generate_multiple_prompts(self, category_key, count):
        prompts = []
        for i in range(count):
            prompt_text = self.generate_prompt(category_key)
            prompts.append({
                "id": i + 1,
                "prompt": prompt_text,
                "category": self.categories[category_key],
                "words": len(prompt_text.split()),
                "characters": len(prompt_text)
            })
        return prompts

    def display_prompts(self, prompts, category_name):
        print(f"\n🎨 GENERATED {len(prompts)} {category_name.upper()} PROMPTS:")
        print("=" * 80)
        
        for prompt_data in prompts:
            print(f"\n#{prompt_data['id']:02d}:")
            print(f"📝 {prompt_data['prompt']}")
            print(f"📊 Words: {prompt_data['words']} | Characters: {prompt_data['characters']}")
            print("-" * 80)

    def save_to_file(self, prompts, category_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{category_name}_prompts_{timestamp}.json"
        
        data = {
            "metadata": {
                "category": category_name,
                "count": len(prompts),
                "generated_at": datetime.now().isoformat(),
                "version": "2.0"
            },
            "prompts": prompts
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filename

    def show_statistics(self, prompts):
        total_words = sum(p['words'] for p in prompts)
        total_chars = sum(p['characters'] for p in prompts)
        avg_words = total_words / len(prompts)
        avg_chars = total_chars / len(prompts)
        
        print(f"\n📊 GENERATION STATISTICS:")
        print(f"   Total prompts: {len(prompts)}")
        print(f"   Average length: {avg_words:.1f} words")
        print(f"   Average characters: {avg_chars:.1f}")
        print(f"   Total words: {total_words}")
        print(f"   Total characters: {total_chars}")

def main():
    generator = UltimatePromptGenerator()
    
    while True:
        category_choice, num_prompts = generator.get_user_input()
        category_name = generator.categories[category_choice].replace('_', ' ').title()
        
        print(f"\n🔄 Generating {num_prompts} {category_name} prompts...")
        prompts = generator.generate_multiple_prompts(category_choice, num_prompts)
        
        generator.display_prompts(prompts, category_name)
        generator.show_statistics(prompts)
        
        save_choice = input("\n💾 Save these prompts to a file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes']:
            filename = generator.save_to_file(prompts, category_name)
            print(f"✅ Prompts saved to: {filename}")
        
        again = input("\n🔄 Generate more prompts? (y/n): ").lower().strip()
        if again not in ['y', 'yes']:
            print("👋 Thank you for using the Ultimate Prompt Generator!")
            break

if __name__ == "__main__":
    main()