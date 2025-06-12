# Function defined
def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling
    
    Args:
        numerator: Number to be divided
        denominator: Number to divide by
        
    Returns:
        Tuple: (success_status, result/error_message)
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return (False, "Error: Both inputs must be numbers")
    
    try:
        result = num / denom
        return (True, result)
    except ZeroDivisionError:
        return (False, "Error: Cannot divide by zero") 
