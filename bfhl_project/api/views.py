from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def bfhl_view(request):
    if request.method == 'POST':
        # Extract data from the request
        data = request.data.get('data', [])
        
        # Initialize the response fields
        numbers = []
        alphabets = []
        highest_lowercase = None

        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                # Check if the character is lowercase
                if item.islower():
                    if highest_lowercase is None or item > highest_lowercase:
                        highest_lowercase = item

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": "venukanthan_b_s_22022002",
            "email": "venukanthan.bs2021@vitstudent.ac.in",
            "roll_number": "21BPS1592",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }

        return Response(response)

    elif request.method == 'GET':
        # Return the operation code
        return Response({"operation_code": 1})
