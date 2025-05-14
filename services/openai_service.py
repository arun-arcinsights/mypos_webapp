import openai
from flask import current_app

'''def generate_quotation(product_type, description, budget=0):
    """
    Generate a professional quotation using OpenAI API
    """
    openai.api_key = current_app.config['OPENAI_API_KEY']
    
    prompt = f"""
    Generate a professional quotation for the following:
    Product/Service Type: {product_type}
    Description: {description}
    
    The quotation should include:
    1. A professional introduction
    2. Detailed breakdown of the product/service
    3. Timeline for delivery
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional quotation generator assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        current_app.logger.error(f"OpenAI API error: {str(e)}")
        return f"Error generating quotation: {str(e)}"

'''

def generate_quotation(product_type, description, budget=0):
    """
    Generate a professional quotation using OpenAI API with precise tabular format
    """
    openai.api_key = current_app.config['OPENAI_API_KEY']
    
    prompt = f"""
    Generate a professional quotation for the following:
    Product/Service Type: {product_type}
    Description: {description}
    
    The quotation should have the following format:
    
    1. A brief professional introduction (2-3 sentences maximum)
    
    2. A precise tabular breakdown of services and costs in this format:
       | Service/Item | Description | Estimated Cost |
       | ------------ | ----------- | -------------- |
       | [Service 1]  | [Brief description] | $X |
       | [Service 2]  | [Brief description] | $X |
       | [Service 3]  | [Brief description] | $X |
       | Total        |               | $TOTAL |
    
    3. A brief timeline for delivery (1-2 sentences)
    
    4. A brief closing note (1-2 sentences)
    
    IMPORTANT: 
    - Do not use placeholders like [Client's Name] or [Your Name]
    - Create realistic, market-appropriate cost estimates for each service
    - Make sure the table is properly formatted with markdown syntax
    - The services should be specific to the type of work requested
    - Include 3-5 service line items that would be typical for this type of work
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional quotation generator assistant that creates precise, tabular quotations with specific service items and costs. You format your response with proper markdown tables and structure."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        current_app.logger.error(f"OpenAI API error: {str(e)}")
        return f"Error generating quotation: {str(e)}"