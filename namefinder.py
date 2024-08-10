import openai

# Initialize the OpenAI API key
openai.api_key = ''

def recommend_names(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative branding specialist."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,  # Increased to capture more content
            temperature=0.7
        )

        # Extract and process the response
        response_text = response.choices[0].message['content'].strip()
        if not response_text:
            print("No names generated.")
            return []

        # Process the response to get names
        name_suggestions = response_text.split('\n')
        filtered_names = [name.strip() for name in name_suggestions if name.strip() and len(name.strip()) <= 10]
        
        if not filtered_names:
            print("No valid names found. Try adjusting the prompt or parameters.")
        
        return filtered_names

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Detailed prompt including the number of names
    prompt = """
 You are an expert branding and naming AI tasked with generating a list of unique and memorable domain names for an innovative educational platform.

Vision: Empowering students to blaze new trails and explore new paths by guiding them to understand their capabilities and reach their full potential. 
Platform Overview: This platform is dedicated to empowering students by guiding them to explore new paths and discover their potential.
Core Features: The platform offers AI-driven guidance, personalized educational resources, a vibrant community for students of each university and also inter-university, and a user-friendly interface that supports students in navigating their educational journeys. It includes features like all university applications at a single platform, and skill-building resources tailored to individual needs.

Name Requirements:  

1. Character Restrictions: The name should be a single continuous string without special characters like hyphens. 
2. Relevance: The name should clearly reflect the themes of education, exploration, empowerment, and student guidance. 
3. Uniqueness: Ensure the name is distinctive and not easily confused with existing brands in the educational sector. 
4. Length and Memorability: Aim for a short name, ideally under ten characters, that is easy to remember and pronounce. 
5. Marketing Potential: The name should support marketing efforts, be easily recognizable, and avoid pitfalls like pluralization confusion. 

Format: single word only with no description
    """

    names = recommend_names(prompt)
    
    if names:
        print("\nRecommended Names:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
    else:
        print("No names were returned.")
