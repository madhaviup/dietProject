from flask import Flask
import controller as dynamodb

app = Flask(__name__)


@app.route('/Receipes/', methods=['GET','POST'])
def get_recipe():
    projectionexp = "RecipeId, RecipeFoodCategory, RecipeType, RecipeName, RecipeIngredient, RecipeNutrient, RecipeStep,  RecipeUrl , RecipeImg"

    response = dynamodb.read_recipe('InfoType', 'Recipe', projectionexp)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        if 'Items' in response:
            return { 'Items': response['Items'] }
        return { 'msg' : 'Item not found!' }
    return {
        'msg': 'Some error occurred',
        'response': response
    }


if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/RecipeData', methods=['POST'])
# def add_Recipe():
#     data = request.get_json()
#     response = dynamodb.write_to_RecipeData(data['id'], data['title'], data['director'])    
#     if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
#         return {
#             'msg': 'Added Recipe successfully',
#         }
#     return {  
#         'msg': 'Some error occcured',
#         'response': response
#     }