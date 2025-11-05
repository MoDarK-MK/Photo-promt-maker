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
                "A professional portrait session in a sun-drenched studio with large north-facing windows casting soft, diffused light across the subject's face, highlighting every contour and expression with natural warmth",
                "Landscape photography at the magical golden hour when the sun kisses the horizon, casting long dramatic shadows and bathing everything in a warm, ethereal glow that enhances textures and colors",
                "Urban exploration photography in abandoned industrial complexes where decay and nature intertwine, with peeling paint, broken windows, and vegetation reclaiming man-made structures",
                "Wildlife photography capturing intimate moments in natural habitats, from predator-prey interactions to nurturing behaviors, with perfect timing and composition",
                "Macro photography revealing the hidden world of tiny subjects where water droplets become crystal balls and insect eyes become complex geometric patterns"
            ],
            "dark_moody": [
                "An abandoned Victorian asylum hallway where peeling wallpaper reveals layers of history, dust motes dance in slivers of light, and shadows hold centuries of untold stories",
                "A fog-enshrouded ancient forest where gnarled trees twist towards a grey sky, mysterious figures move between trunks, and the air feels heavy with forgotten secrets",
                "A rain-slicked cobblestone alley in the dead of night where a single flickering gas lamp casts long, dancing shadows and reflections create a distorted reality",
                "Gothic cathedral crypt with vaulted ceilings, intricate stone carvings worn smooth by time, and candlelight that barely illuminates the profound darkness between pillars",
                "Industrial ruins at twilight where rusted machinery creates skeletal silhouettes against a bruised sky, and pools of rainwater mirror the decaying beauty"
            ]
        }

        self.detailed_descriptors = {
            "lighting": [
                "cinematic volumetric lighting with visible light rays cutting through atmospheric haze",
                "dramatic chiaroscuro lighting creating strong contrasts between deep shadows and brilliant highlights",
                "soft diffused lighting that wraps around subjects creating gentle transitions and minimal shadows",
                "hard directional lighting casting sharp, defined shadows that emphasize texture and form",
                "backlighting that creates glowing edges and silhouettes while revealing translucency",
                "side lighting that sculpts subjects with dramatic shadows revealing texture and depth",
                "top lighting that creates downward shadows adding mystery and drama to scenes",
                "bottom lighting that creates unnatural, dramatic upward shadows for eerie effects",
                "natural ambient lighting that feels authentic and true to the environment",
                "studio quality controlled lighting with multiple light sources creating perfect illumination"
            ],
            "composition": [
                "rule of thirds composition with key elements positioned at intersection points for balance",
                "golden ratio spiral composition that naturally guides the viewer's eye through the image",
                "symmetrical composition creating perfect balance and harmony with mirror-like precision",
                "asymmetrical composition using visual weight to create dynamic, engaging balance",
                "leading lines composition using natural and architectural elements to guide viewing path",
                "frame within frame composition using architectural elements to create layered depth",
                "negative space composition where empty areas emphasize the main subject powerfully",
                "diagonal composition creating dynamic tension and movement across the frame",
                "centered composition placing the main subject squarely in the middle for impact",
                "layered composition with foreground, midground, and background elements creating depth"
            ],
            "texture": [
                "highly detailed surface textures showing every scratch, grain, and imperfection realistically",
                "smooth polished surfaces reflecting light with mirror-like clarity and precision",
                "rough textured surfaces catching light and creating complex shadow patterns",
                "transparent materials revealing inner structures and creating refraction effects",
                "translucent materials scattering light softly and creating glowing effects",
                "metallic surfaces with polished, brushed, or weathered finishes catching light",
                "organic textures showing natural patterns, growth rings, and biological structures",
                "fabric textures from rough burlap to smooth silk with visible weave patterns",
                "liquid surfaces with ripples, droplets, and surface tension effects",
                "atmospheric textures like fog, smoke, or haze that affect light transmission"
            ],
            "color": [
                "vibrant saturated color palette with intense, pure hues that command attention",
                "muted desaturated color palette with soft, subtle tones creating calm atmosphere",
                "monochromatic color scheme using variations of a single hue for harmony",
                "complementary color scheme using opposite colors for dynamic contrast",
                "analogous color scheme using neighboring colors for harmonious transitions",
                "warm color palette dominated by reds, oranges, and yellows creating energy",
                "cool color palette dominated by blues, greens, and purples creating calm",
                "pastel color palette with soft, light tones creating gentle, dreamy moods",
                "earth tone color palette using natural browns, greens, and tans for organic feel",
                "neon color palette with electric, glowing colors for futuristic or urban feels"
            ],
            "atmosphere": [
                "heavy atmospheric perspective with depth created through color and value changes",
                "crisp clear atmosphere where distant objects remain sharp and detailed",
                "misty foggy atmosphere softening edges and creating mysterious moods",
                "smoky hazy atmosphere diffusing light and creating dreamlike qualities",
                "rainy wet atmosphere with reflections and saturated colors after showers",
                "dusty sandy atmosphere with particulate matter visible in light beams",
                "steamy humid atmosphere with moisture affecting light and visibility",
                "stormy turbulent atmosphere with dramatic clouds and changing light conditions",
                "calm serene atmosphere with still air and perfect visibility",
                "otherworldly alien atmosphere with unusual lighting and atmospheric effects"
            ]
        }

        self.technical_specs = {
            "camera": [
                "shot on medium format digital camera with incredible dynamic range and detail",
                "captured with full frame DSLR using professional L-series lenses",
                "photographed with mirrorless camera system featuring advanced eye-tracking AF",
                "taken with vintage film camera producing organic grain and color characteristics",
                "created with high-resolution digital back on technical camera for architecture",
                "shot with cinema camera producing cinematic color science and motion",
                "captured using smartphone computational photography with multi-frame processing",
                "photographed with specialized equipment for macro or scientific imaging",
                "taken with waterproof housing for underwater photography applications",
                "created using drone photography for unique aerial perspectives"
            ],
            "lens": [
                "using ultra-wide angle lens for dramatic perspectives and expansive views",
                "with standard prime lens reproducing natural human eye perspective",
                "using telephoto lens for compression effects and distant subject isolation",
                "with macro lens capable of 1:1 reproduction revealing microscopic details",
                "using tilt-shift lens for perspective control and miniature effects",
                "with fast aperture prime lens creating extremely shallow depth of field",
                "using zoom lens covering multiple focal lengths for composition flexibility",
                "with specialty lens producing unique optical characteristics and flares",
                "using anamorphic lens creating cinematic widescreen aspect ratios",
                "with vintage lens producing characteristic rendering and bokeh qualities"
            ],
            "settings": [
                "shot at wide aperture creating extremely shallow depth of field with creamy bokeh",
                "using small aperture for maximum depth of field with front-to-back sharpness",
                "with long exposure creating motion blur and smooth water/cloud effects",
                "using high-speed sync flash freezing fast action with perfect illumination",
                "with multiple exposure technique combining several images in-camera",
                "using HDR technique capturing extended dynamic range from shadows to highlights",
                "with focus stacking technique combining multiple focus distances for sharpness",
                "using panoramic stitching creating ultra-wide aspect ratio compositions",
                "with time-lapse sequence capturing changing light and motion over time",
                "using infrared conversion capturing invisible light spectrum for surreal effects"
            ]
        }

        self.artistic_styles = [
            "hyperrealistic style where every detail is rendered with photographic accuracy",
            "photorealistic CGI rendering indistinguishable from actual photography",
            "cinematic style with dramatic lighting and color grading reminiscent of films",
            "painterly style emulating traditional oil painting techniques and brushwork",
            "impressionistic style capturing light and mood rather than precise details",
            "expressionistic style distorting reality to convey emotional experience",
            "surreal style combining realistic elements in impossible dreamlike arrangements",
            "abstract style focusing on shapes, colors, and forms rather than representation",
            "conceptual style where the idea behind the image is as important as the image itself",
            "minimalist style using extreme simplification to essential elements only",
            "maximalist style embracing complexity, detail, and visual abundance",
            "brutalist style emphasizing raw materials and structural honesty",
            "art deco style with geometric patterns, luxury materials, and streamlined forms",
            "art nouveau style featuring organic forms, curved lines, and natural motifs",
            "baroque style with dramatic movement, rich detail, and strong emotional content",
            "renaissance style emphasizing classical proportion, balance, and humanism",
            "romantic style focusing on emotion, drama, and the sublime in nature",
            "gothic style with verticality, intricate detail, and mystical atmosphere",
            "byzantine style featuring rich color, gold backgrounds, and spiritual themes",
            "modernist style breaking with tradition through abstraction and innovation"
        ]

        self.quality_descriptors = [
            "ultra detailed 8K resolution with incredible sharpness and clarity",
            "hyperrealistic rendering indistinguishable from high-end photography",
            "masterpiece quality worthy of gallery exhibition and critical acclaim",
            "award-winning composition and execution at professional level",
            "trending on artstation with exceptional artistic and technical merit",
            "unreal engine 5 rendering with lumen global illumination and nanite geometry",
            "octane render with physically accurate lighting and material properties",
            "v-ray rendering with advanced ray tracing and global illumination",
            "arnold renderer producing cinematic quality with natural lighting",
            "cycles rendering with node-based materials and realistic light transport",
            "eevee real-time rendering with impressive quality and performance",
            "photorealistic quality that challenges perception of reality",
            "cinematic quality matching big-budget film production values",
            "studio quality with perfect lighting and professional execution",
            "commercial grade suitable for high-end advertising campaigns",
            "editorial quality meeting standards for premium magazine features",
            "fine art quality with artistic vision and technical excellence",
            "gallery quality presentation ready for exhibition in prestigious spaces",
            "museum quality preservation and presentation standards",
            "exhibition quality large format printing with incredible detail"
        ]

        self.mood_enhancers = [
            "creating intense emotional impact that resonates deeply with viewers",
            "evoking powerful nostalgia and memories through visual storytelling",
            "generating sense of wonder and amazement at beauty and complexity",
            "profound spiritual atmosphere that transcends ordinary experience",
            "dramatic tension that creates anticipation and emotional engagement",
            "peaceful serenity that calms the mind and soothes the spirit",
            "chaotic energy that feels alive, dynamic, and unpredictable",
            "orderly harmony where every element feels perfectly placed and balanced",
            "mysterious atmosphere inviting curiosity and deeper exploration",
            "joyful celebration of life, color, and positive energy",
            "melancholic beauty found in transient moments and fading glory",
            "epic scale that emphasizes grandeur and monumental significance",
            "intimate connection that feels personal and emotionally immediate",
            "alien strangeness that challenges perceptions of normal reality",
            "familiar comfort that feels like returning to a cherished memory"
        ]

        self.detail_enhancers = [
            "micro-detail rendering where even the smallest elements are fully realized",
            "texture mapping showing realistic surface properties and material characteristics",
            "subsurface scattering simulating light penetration through translucent materials",
            "specular highlights showing precise reflection of light sources",
            "ambient occlusion creating natural shadowing in corners and crevices",
            "global illumination with accurate light bouncing and color bleeding",
            "caustics rendering showing light focusing through reflective/refractive surfaces",
            "depth of field simulation with accurate bokeh and focus transitions",
            "motion blur capturing the illusion of movement and passage of time",
            "volumetric lighting with light beams, god rays, and atmospheric effects",
            "particle systems showing dust, smoke, sparks, or other small elements",
            "fluid simulation with realistic water, smoke, or fire behavior",
            "cloth simulation showing realistic folding, draping, and movement",
            "hair and fur rendering with individual strands and natural behavior",
            "weathering effects showing age, wear, and environmental interaction"
        ]

    def get_user_input(self):
        print("🎨 ULTIMATE ADVANCED PROMPT GENERATOR")
        print("=" * 70)
        
        print("\nAVAILABLE CATEGORIES (45 OPTIONS):")
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
        
        return category_choice, num_prompts

    def generate_detailed_prompt(self, category_key):
        category = self.categories[category_key]
        
        prompt_parts = []
        
        scene_base = random.choice(list(self.scene_elements.values())[0])
        prompt_parts.append(scene_base)
        
        lighting_desc = random.choice(self.detailed_descriptors["lighting"])
        prompt_parts.append(lighting_desc)
        
        composition_desc = random.choice(self.detailed_descriptors["composition"])
        prompt_parts.append(composition_desc)
        
        for _ in range(3):
            texture_desc = random.choice(self.detailed_descriptors["texture"])
            prompt_parts.append(texture_desc)
        
        color_desc = random.choice(self.detailed_descriptors["color"])
        prompt_parts.append(color_desc)
        
        atmosphere_desc = random.choice(self.detailed_descriptors["atmosphere"])
        prompt_parts.append(atmosphere_desc)
        
        artistic_style = random.choice(self.artistic_styles)
        prompt_parts.append(artistic_style)
        
        camera_spec = random.choice(self.technical_specs["camera"])
        prompt_parts.append(camera_spec)
        
        lens_spec = random.choice(self.technical_specs["lens"])
        prompt_parts.append(lens_spec)
        
        settings_spec = random.choice(self.technical_specs["settings"])
        prompt_parts.append(settings_spec)
        
        quality_desc = random.choice(self.quality_descriptors)
        prompt_parts.append(quality_desc)
        
        mood_enhancer = random.choice(self.mood_enhancers)
        prompt_parts.append(mood_enhancer)
        
        for _ in range(4):
            detail_enhancer = random.choice(self.detail_enhancers)
            prompt_parts.append(detail_enhancer)
        
        random.shuffle(prompt_parts)
        
        final_prompt = ". ".join(prompt_parts) + "."
        
        word_count = len(final_prompt.split())
        if word_count < 100:
            additional_details = []
            while word_count < 100:
                extra_detail = random.choice(self.detail_enhancers + self.mood_enhancers)
                if extra_detail not in prompt_parts:
                    additional_details.append(extra_detail)
                    word_count = len((". ".join(prompt_parts + additional_details) + ".").split())
            
            prompt_parts.extend(additional_details)
            final_prompt = ". ".join(prompt_parts) + "."
        
        return final_prompt

    def generate_multiple_prompts(self, category_key, count):
        prompts = []
        for i in range(count):
            prompt_text = self.generate_detailed_prompt(category_key)
            word_count = len(prompt_text.split())
            char_count = len(prompt_text)
            
            prompts.append({
                "id": i + 1,
                "prompt": prompt_text,
                "category": self.categories[category_key],
                "words": word_count,
                "characters": char_count,
                "detail_level": "high" if word_count > 150 else "medium"
            })
        return prompts

    def display_prompts(self, prompts, category_name):
        print(f"\n🎨 GENERATED {len(prompts)} {category_name.upper()} PROMPTS:")
        print("=" * 100)
        
        for prompt_data in prompts:
            print(f"\n#{prompt_data['id']:03d} [{prompt_data['detail_level'].upper()} DETAIL]:")
            print(f"📝 {prompt_data['prompt']}")
            print(f"📊 Words: {prompt_data['words']} | Characters: {prompt_data['characters']}")
            print("-" * 100)

    def save_to_file(self, prompts, category_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ADVANCED_{category_name}_prompts_{timestamp}.json"
        
        data = {
            "metadata": {
                "category": category_name,
                "count": len(prompts),
                "generated_at": datetime.now().isoformat(),
                "version": "3.0",
                "detail_level": "advanced",
                "total_words": sum(p['words'] for p in prompts),
                "average_words": sum(p['words'] for p in prompts) / len(prompts)
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
        
        high_detail = sum(1 for p in prompts if p['detail_level'] == 'high')
        
        print(f"\n📊 ADVANCED GENERATION STATISTICS:")
        print(f"   Total prompts: {len(prompts)}")
        print(f"   High detail prompts: {high_detail}")
        print(f"   Average length: {avg_words:.1f} words")
        print(f"   Average characters: {avg_chars:.1f}")
        print(f"   Total words generated: {total_words}")
        print(f"   Total characters: {total_chars}")
        print(f"   Minimum words: {min(p['words'] for p in prompts)}")
        print(f"   Maximum words: {max(p['words'] for p in prompts)}")

def main():
    generator = UltimatePromptMaster()
    
    while True:
        category_choice, num_prompts = generator.get_user_input()
        category_name = generator.categories[category_choice].replace('_', ' ').title()
        
        print(f"\n🔄 Generating {num_prompts} advanced {category_name} prompts...")
        print("This may take a moment for high-detail prompts...")
        
        prompts = generator.generate_multiple_prompts(category_choice, num_prompts)
        
        generator.display_prompts(prompts, category_name)
        generator.show_statistics(prompts)
        
        save_choice = input("\n💾 Save these advanced prompts to a file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes']:
            filename = generator.save_to_file(prompts, category_name)
            print(f"✅ Advanced prompts saved to: {filename}")
        
        again = input("\n🔄 Generate more advanced prompts? (y/n): ").lower().strip()
        if again not in ['y', 'yes']:
            print("👋 Thank you for using the Ultimate Advanced Prompt Generator!")
            break

if __name__ == "__main__":
    main()