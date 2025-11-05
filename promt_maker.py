import random
import json
import math
from datetime import datetime
from enum import Enum

class WeatherType(Enum):
    SUNNY = "sunny"
    CLOUDY = "cloudy"
    RAINY = "rainy"
    STORMY = "stormy"
    FOGGY = "foggy"
    SNOWY = "snowy"
    WINDY = "windy"
    MISTY = "misty"

class TimeOfDay(Enum):
    DAWN = "dawn"
    MORNING = "morning"
    NOON = "noon"
    AFTERNOON = "afternoon"
    GOLDEN_HOUR = "golden_hour"
    BLUE_HOUR = "blue_hour"
    NIGHT = "night"
    MIDNIGHT = "midnight"

class MaterialType(Enum):
    METAL = "metal"
    WOOD = "wood"
    STONE = "stone"
    GLASS = "glass"
    FABRIC = "fabric"
    LIQUID = "liquid"
    SKIN = "skin"
    HAIR = "hair"
    EYES = "eyes"
    FOLIAGE = "foliage"

class AdvancedPromptGenerator:
    def __init__(self):
        self.setup_parametric_system()
        self.setup_weather_lighting()
        self.setup_material_system()
        self.setup_3d_composition()
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

    def setup_parametric_system(self):
        self.parametric_controls = {
            "detail_level": {
                "min": 1, "max": 10, "default": 8,
                "descriptions": {
                    1: "minimal details, basic shapes only",
                    3: "moderate details, recognizable forms",
                    5: "good details, clear textures",
                    7: "high details, intricate elements", 
                    9: "ultra details, microscopic precision",
                    10: "hyper-realistic, beyond human perception"
                }
            },
            "complexity": {
                "min": 1, "max": 10, "default": 7,
                "descriptions": {
                    1: "extremely simple, single subject",
                    3: "simple composition, few elements",
                    5: "moderate complexity, balanced elements",
                    7: "complex arrangement, multiple focal points",
                    9: "highly complex, intricate relationships",
                    10: "overwhelming complexity, maximalist approach"
                }
            },
            "realism": {
                "min": 1, "max": 10, "default": 8,
                "descriptions": {
                    1: "completely abstract, non-representational",
                    3: "stylized, artistic interpretation",
                    5: "semi-realistic, believable but artistic",
                    7: "realistic, convincing representation",
                    9: "photorealistic, indistinguishable from photo",
                    10: "hyper-realistic, enhanced reality"
                }
            },
            "saturation": {
                "min": 1, "max": 10, "default": 6,
                "descriptions": {
                    1: "completely desaturated, grayscale",
                    3: "muted colors, subtle tones",
                    5: "natural saturation, true to life",
                    7: "vibrant colors, enhanced reality",
                    9: "highly saturated, intense colors",
                    10: "oversaturated, surreal color palette"
                }
            },
            "contrast": {
                "min": 1, "max": 10, "default": 7,
                "descriptions": {
                    1: "extremely low contrast, flat appearance",
                    3: "low contrast, soft and gentle",
                    5: "medium contrast, balanced tones",
                    7: "high contrast, dramatic tones",
                    9: "very high contrast, bold separation",
                    10: "extreme contrast, black and white extremes"
                }
            },
            "sharpness": {
                "min": 1, "max": 10, "default": 8,
                "descriptions": {
                    1: "extremely soft, dreamlike blur",
                    3: "soft focus, gentle edges",
                    5: "moderate sharpness, natural appearance",
                    7: "sharp focus, clear details",
                    9: "very sharp, crisp edges",
                    10: "ultra sharp, razor-sharp details"
                }
            }
        }

    def setup_weather_lighting(self):
        self.weather_systems = {
            WeatherType.SUNNY: {
                "lighting": "bright direct sunlight with sharp shadows",
                "atmosphere": "clear visibility with minimal atmospheric interference",
                "color_temperature": "warm golden tones around 5500K",
                "effects": ["lens flare", "strong highlights", "deep shadows", "high dynamic range"]
            },
            WeatherType.CLOUDY: {
                "lighting": "soft diffused light with minimal shadows",
                "atmosphere": "even lighting with gentle contrast",
                "color_temperature": "cool neutral tones around 6500K", 
                "effects": ["soft shadows", "reduced contrast", "muted colors", "gentle transitions"]
            },
            WeatherType.RAINY: {
                "lighting": "low contrast flat lighting with reflective surfaces",
                "atmosphere": "moist air with reduced visibility",
                "color_temperature": "cool blue tones around 7000K",
                "effects": ["water reflections", "surface wetness", "atmospheric haze", "saturated colors"]
            },
            WeatherType.STORMY: {
                "lighting": "dramatic directional lighting with lightning bursts",
                "atmosphere": "heavy atmosphere with dramatic clouds",
                "color_temperature": "cool dramatic tones around 8000K",
                "effects": ["lightning flashes", "dark moody tones", "high contrast", "dramatic shadows"]
            },
            WeatherType.FOGGY: {
                "lighting": "extremely diffused almost shadowless light",
                "atmosphere": "thick fog reducing visibility significantly",
                "color_temperature": "cool muted tones around 7500K",
                "effects": ["atmospheric perspective", "soft edges", "muted colors", "mysterious ambiance"]
            },
            WeatherType.SNOWY: {
                "lighting": "bright reflective light from snow coverage",
                "atmosphere": "crisp clean air with snow particles",
                "color_temperature": "cool bright tones around 6000K",
                "effects": ["snow reflections", "bright highlights", "clean whites", "sparkling surfaces"]
            }
        }

        self.time_lighting = {
            TimeOfDay.DAWN: {
                "light_angle": "low horizontal light from the east",
                "color": "soft pink and orange hues with blue shadows",
                "intensity": "gentle increasing light",
                "characteristics": ["long shadows", "warm highlights", "cool shadows", "dramatic contrast"]
            },
            TimeOfDay.MORNING: {
                "light_angle": "moderate angle from east-southeast", 
                "color": "clean bright white light with slight warmth",
                "intensity": "bright clear light",
                "characteristics": ["balanced shadows", "natural colors", "good visibility", "fresh appearance"]
            },
            TimeOfDay.NOON: {
                "light_angle": "direct overhead light",
                "color": "neutral white light minimal color cast",
                "intensity": "maximum brightness harsh light",
                "characteristics": ["short shadows", "high contrast", "washed out colors", "technical lighting"]
            },
            TimeOfDay.GOLDEN_HOUR: {
                "light_angle": "low angle from west",
                "color": "rich golden orange warm tones",
                "intensity": "soft directional light",
                "characteristics": ["extremely long shadows", "warm glow", "dramatic lighting", "cinematic quality"]
            },
            TimeOfDay.BLUE_HOUR: {
                "light_angle": "twilight minimal direct light",
                "color": "cool blue and purple tones",
                "intensity": "low ambient light",
                "characteristics": ["minimal shadows", "cool colors", "moody atmosphere", "urban lights visible"]
            },
            TimeOfDay.NIGHT: {
                "light_angle": "artificial light sources only",
                "color": "mixed color temperatures from artificial lights",
                "intensity": "very low light high contrast",
                "characteristics": ["deep shadows", "localized lighting", "high ISO grain", "moody ambiance"]
            }
        }

    def setup_material_system(self):
        self.material_library = {
            MaterialType.METAL: {
                "properties": ["reflectivity", "conductivity", "malleability", "strength"],
                "types": {
                    "polished_steel": {
                        "reflectivity": 0.85,
                        "roughness": 0.05,
                        "color": "silver_gray",
                        "characteristics": ["mirror-like finish", "sharp reflections", "clean lines", "industrial aesthetic"]
                    },
                    "rusted_iron": {
                        "reflectivity": 0.15,
                        "roughness": 0.8,
                        "color": "orange_brown",
                        "characteristics": ["textured surface", "irregular patterns", "aged appearance", "industrial decay"]
                    },
                    "brushed_aluminum": {
                        "reflectivity": 0.6,
                        "roughness": 0.3,
                        "color": "light_gray",
                        "characteristics": ["directional grain", "soft reflections", "modern appearance", "technical finish"]
                    },
                    "copper_patina": {
                        "reflectivity": 0.4,
                        "roughness": 0.6,
                        "color": "green_blue",
                        "characteristics": ["oxidized surface", "color variation", "aged elegance", "organic patterns"]
                    }
                }
            },
            MaterialType.WOOD: {
                "properties": ["grain_pattern", "hardness", "porosity", "flexibility"],
                "types": {
                    "oak_wood": {
                        "grain_pattern": "pronounced_linear",
                        "hardness": "high",
                        "color": "light_brown",
                        "characteristics": ["strong grain", "durable surface", "traditional appearance", "warm tones"]
                    },
                    "walnut_wood": {
                        "grain_pattern": "rich_figured",
                        "hardness": "medium_high", 
                        "color": "dark_brown",
                        "characteristics": ["elegant grain", "deep colors", "luxury appearance", "smooth finish"]
                    },
                    "driftwood": {
                        "grain_pattern": "weathered_irregular",
                        "hardness": "weathered",
                        "color": "pale_gray",
                        "characteristics": ["smooth texture", "soft edges", "organic shapes", "natural aging"]
                    }
                }
            },
            MaterialType.GLASS: {
                "properties": ["transparency", "reflectivity", "refraction", "surface_quality"],
                "types": {
                    "crystal_glass": {
                        "transparency": 0.95,
                        "refraction": 1.5,
                        "color": "clear",
                        "characteristics": ["high clarity", "sharp edges", "brilliant reflections", "premium quality"]
                    },
                    "frosted_glass": {
                        "transparency": 0.4,
                        "refraction": 1.5,
                        "color": "white_diffused",
                        "characteristics": ["soft diffusion", "reduced clarity", "gentle lighting", "privacy effect"]
                    },
                    "stained_glass": {
                        "transparency": 0.7,
                        "refraction": 1.5,
                        "color": "colored_patterns",
                        "characteristics": ["vibrant colors", "decorative patterns", "light transmission", "artistic design"]
                    }
                }
            },
            MaterialType.SKIN: {
                "properties": ["subsurface_scattering", "pore_detail", "moisture_level", "texture"],
                "types": {
                    "youthful_skin": {
                        "subsurface_scattering": 0.7,
                        "pore_detail": "fine",
                        "characteristics": ["smooth texture", "even tone", "natural glow", "healthy appearance"]
                    },
                    "aged_skin": {
                        "subsurface_scattering": 0.5,
                        "pore_detail": "pronounced",
                        "characteristics": ["wrinkles", "age_spots", "textured surface", "character lines"]
                    },
                    "fantasy_skin": {
                        "subsurface_scattering": 0.8,
                        "pore_detail": "unique",
                        "characteristics": ["unnatural colors", "special patterns", "magical glow", "otherworldly texture"]
                    }
                }
            }
        }

    def setup_3d_composition(self):
        self.camera_systems = {
            "perspective": {
                "focal_lengths": {
                    "ultra_wide": {"mm": 14, "characteristics": ["dramatic perspective", "distorted edges", "expansive view"]},
                    "wide_angle": {"mm": 24, "characteristics": ["natural perspective", "good for environments", "slight distortion"]},
                    "standard": {"mm": 50, "characteristics": ["natural view", "minimal distortion", "versatile"]},
                    "portrait": {"mm": 85, "characteristics": ["flattering compression", "background separation", "natural proportions"]},
                    "telephoto": {"mm": 200, "characteristics": ["compressed perspective", "background magnification", "isolation"]}
                },
                "aperture_settings": {
                    "f1.4": {"dof": "very_shallow", "characteristics": ["extreme background blur", "narrow focus plane", "dreamy quality"]},
                    "f2.8": {"dof": "shallow", "characteristics": ["strong background separation", "artistic blur", "professional look"]},
                    "f5.6": {"dof": "moderate", "characteristics": ["balanced focus", "recognizable background", "versatile"]},
                    "f11": {"dof": "deep", "characteristics": ["extended focus", "detailed background", "landscape suitable"]},
                    "f22": {"dof": "maximum", "characteristics": ["everything in focus", "technical precision", "specialized use"]}
                }
            },
            "lighting_setups": {
                "three_point": {
                    "lights": ["key", "fill", "back"],
                    "characteristics": ["balanced illumination", "dimensional quality", "professional standard"]
                },
                "rim_lighting": {
                    "lights": ["back_light_primary"],
                    "characteristics": ["dramatic edges", "strong separation", "moody atmosphere"]
                },
                "softbox_lighting": {
                    "lights": ["large_diffused_source"],
                    "characteristics": ["gentle shadows", "even illumination", "flattering light"]
                },
                "chiaroscuro": {
                    "lights": ["single_directional"],
                    "characteristics": ["high contrast", "dramatic shadows", "painterly quality"]
                }
            },
            "render_engines": {
                "unreal_engine_5": {
                    "features": ["lumen_gi", "nanite_geometry", "virtual_shadow_maps"],
                    "characteristics": ["real-time global illumination", "infinite geometric detail", "cinematic quality"]
                },
                "octane_render": {
                    "features": ["spectral_rendering", "true_displacement", "advanced_materials"],
                    "characteristics": ["physically accurate", "fast gpu rendering", "production quality"]
                },
                "vray": {
                    "features": ["adaptive_lighting", "progressive_rendering", "advanced_materials"],
                    "characteristics": ["photorealistic results", "industry standard", "versatile lighting"]
                },
                "arnold": {
                    "features": ["physical_sky", "standard_surface", "deep_image_output"],
                    "characteristics": ["movie production quality", "natural lighting", "robust rendering"]
                }
            }
        }

    def generate_parametric_description(self, params=None):
        if params is None:
            params = {}
        
        parametric_desc = []
        
        for param_name, config in self.parametric_controls.items():
            value = params.get(param_name, config["default"])
            value = max(config["min"], min(config["max"], value))
            
            description = config["descriptions"].get(
                value, 
                f"{param_name} level {value}"
            )
            parametric_desc.append(description)
        
        return ", ".join(parametric_desc)

    def generate_weather_lighting_description(self):
        weather = random.choice(list(WeatherType))
        time_of_day = random.choice(list(TimeOfDay))
        
        weather_info = self.weather_systems[weather]
        time_info = self.time_lighting[time_of_day]
        
        description = (
            f"{weather.value} weather conditions with {weather_info['lighting']} "
            f"during {time_of_day.value} creating {time_info['color']}. "
            f"Features include {random.choice(weather_info['effects'])} and "
            f"{random.choice(time_info['characteristics'])}"
        )
        
        return description

    def generate_material_description(self, material_count=3):
        materials = random.sample(list(MaterialType), min(material_count, len(MaterialType)))
        material_descriptions = []
        
        for material_type in materials:
            material_data = self.material_library[material_type]
            material_subtype = random.choice(list(material_data["types"].keys()))
            subtype_data = material_data["types"][material_subtype]
            
            desc = (
                f"{material_subtype.replace('_', ' ')} {material_type.value} with "
                f"{random.choice(subtype_data['characteristics'])} and "
                f"{material_data['properties'][0]} of {subtype_data.get(material_data['properties'][0], 'natural')}"
            )
            material_descriptions.append(desc)
        
        return "; ".join(material_descriptions)

    def generate_3d_composition_description(self):
        camera = random.choice(list(self.camera_systems["perspective"]["focal_lengths"].keys()))
        aperture = random.choice(list(self.camera_systems["perspective"]["aperture_settings"].keys()))
        lighting = random.choice(list(self.camera_systems["lighting_setups"].keys()))
        render_engine = random.choice(list(self.camera_systems["render_engines"].keys()))
        
        camera_info = self.camera_systems["perspective"]["focal_lengths"][camera]
        aperture_info = self.camera_systems["perspective"]["aperture_settings"][aperture]
        lighting_info = self.camera_systems["lighting_setups"][lighting]
        render_info = self.camera_systems["render_engines"][render_engine]
        
        description = (
            f"3D composition using {camera} perspective ({camera_info['mm']}mm equivalent) "
            f"with {aperture} aperture creating {aperture_info['dof']} depth of field. "
            f"{lighting.replace('_', ' ')} lighting setup providing {random.choice(lighting_info['characteristics'])}. "
            f"Rendered in {render_engine.replace('_', ' ')} with {random.choice(render_info['features'])} "
            f"for {random.choice(render_info['characteristics'])}"
        )
        
        return description

    def get_user_input(self):
        print("🎨 ADVANCED PARAMETRIC PROMPT GENERATOR")
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
        
        print("\n🎛️  PARAMETRIC CONTROLS (press enter for defaults):")
        params = {}
        for param_name, config in self.parametric_controls.items():
            while True:
                try:
                    value_input = input(f"{param_name.title()} ({config['min']}-{config['max']}, default {config['default']}): ").strip()
                    if not value_input:
                        value = config["default"]
                        break
                    value = int(value_input)
                    if config["min"] <= value <= config["max"]:
                        break
                    print(f"Please enter a number between {config['min']} and {config['max']}")
                except:
                    print("Invalid input. Please enter a number.")
            params[param_name] = value
        
        return category_choice, num_prompts, params

    def generate_advanced_prompt(self, category_key, params):
        category = self.categories[category_key]
        
        components = []
        
        parametric_desc = self.generate_parametric_description(params)
        components.append(f"Parametric settings: {parametric_desc}")
        
        weather_lighting = self.generate_weather_lighting_description()
        components.append(f"Weather and lighting: {weather_lighting}")
        
        materials = self.generate_material_description()
        components.append(f"Material system: {materials}")
        
        composition_3d = self.generate_3d_composition_description()
        components.append(f"3D composition: {composition_3d}")
        
        base_scene = self.generate_base_scene(category)
        components.append(f"Scene: {base_scene}")
        
        final_prompt = ". ".join(components) + "."
        
        word_count = len(final_prompt.split())
        if word_count < 100:
            additional_details = self.generate_additional_details()
            components.append(f"Additional details: {additional_details}")
            final_prompt = ". ".join(components) + "."
        
        return final_prompt

    def generate_base_scene(self, category):
        scenes = {
            "photography": "professional photoshoot in controlled studio environment",
            "fantasy": "epic fantasy landscape with magical elements and mythical creatures",
            "sci_fi": "futuristic environment with advanced technology and alien architecture",
            "portrait": "intimate portrait session capturing personality and emotion",
            "landscape": "breathtaking natural scenery with dramatic geological formations"
        }
        return scenes.get(category, f"creative {category} scene with artistic composition")

    def generate_additional_details(self):
        details = [
            "intricate surface details with micro-textures and fine imperfections",
            "advanced particle systems showing atmospheric effects and dynamic elements",
            "complex shader networks creating realistic material interactions",
            "dynamic lighting rigs with multiple light sources and color temperatures",
            "high-poly geometry with optimized topology for realistic deformation"
        ]
        return random.choice(details)

    def generate_multiple_prompts(self, category_key, count, params):
        prompts = []
        for i in range(count):
            prompt_text = self.generate_advanced_prompt(category_key, params)
            word_count = len(prompt_text.split())
            char_count = len(prompt_text)
            
            prompts.append({
                "id": i + 1,
                "prompt": prompt_text,
                "category": self.categories[category_key],
                "words": word_count,
                "characters": char_count,
                "parameters": params,
                "detail_level": "ultra" if word_count > 200 else "high"
            })
        return prompts

    def display_prompts(self, prompts, category_name):
        print(f"\n🎨 GENERATED {len(prompts)} ADVANCED {category_name.upper()} PROMPTS:")
        print("=" * 120)
        
        for prompt_data in prompts:
            print(f"\n#{prompt_data['id']:03d} [{prompt_data['detail_level'].upper()} DETAIL]:")
            print(f"📝 {prompt_data['prompt']}")
            print(f"📊 Words: {prompt_data['words']} | Characters: {prompt_data['characters']}")
            print("⚙️  Parameters:", prompt_data['parameters'])
            print("-" * 120)

    def save_to_file(self, prompts, category_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ADVANCED_PARAMETRIC_{category_name}_prompts_{timestamp}.json"
        
        data = {
            "metadata": {
                "category": category_name,
                "count": len(prompts),
                "generated_at": datetime.now().isoformat(),
                "version": "4.0",
                "detail_level": "parametric_advanced",
                "systems_used": ["parametric", "weather_lighting", "material", "3d_composition"],
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
        
        ultra_detail = sum(1 for p in prompts if p['detail_level'] == 'ultra')
        
        print(f"\n📊 ADVANCED PARAMETRIC STATISTICS:")
        print(f"   Total prompts: {len(prompts)}")
        print(f"   Ultra detail prompts: {ultra_detail}")
        print(f"   Average length: {avg_words:.1f} words")
        print(f"   Average characters: {avg_chars:.1f}")
        print(f"   Total words generated: {total_words}")
        print(f"   Total characters: {total_chars}")
        print(f"   Minimum words: {min(p['words'] for p in prompts)}")
        print(f"   Maximum words: {max(p['words'] for p in prompts)}")
        print(f"   Systems integrated: Parametric, Weather/Lighting, Material, 3D Composition")

def main():
    generator = AdvancedPromptGenerator()
    
    while True:
        category_choice, num_prompts, params = generator.get_user_input()
        category_name = generator.categories[category_choice].replace('_', ' ').title()
        
        print(f"\n🔄 Generating {num_prompts} advanced parametric {category_name} prompts...")
        print("This will integrate all advanced systems: Parametric, Weather/Lighting, Material, and 3D Composition...")
        
        prompts = generator.generate_multiple_prompts(category_choice, num_prompts, params)
        
        generator.display_prompts(prompts, category_name)
        generator.show_statistics(prompts)
        
        save_choice = input("\n💾 Save these advanced parametric prompts to a file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes']:
            filename = generator.save_to_file(prompts, category_name)
            print(f"✅ Advanced parametric prompts saved to: {filename}")
        
        again = input("\n🔄 Generate more advanced parametric prompts? (y/n): ").lower().strip()
        if again not in ['y', 'yes']:
            print("👋 Thank you for using the Advanced Parametric Prompt Generator!")
            break

if __name__ == "__main__":
    main()