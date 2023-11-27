from flask import Flask, request, jsonify
from azure.core.credentials import AzureNamedKeyCredential
from azure.data.tables import TableServiceClient
from flask_cors import CORS
import os


TABLE_NAME = os.environ["AZURE_TABLE_NAME"]
ACCESS_KEY = os.environ["ACCESS_KEY"]
STORAGE_ACC_ENDPOINT = os.environ["STORAGE_ACCOUNT_ENDPOINT"]


credential = AzureNamedKeyCredential(TABLE_NAME, ACCESS_KEY)

service = TableServiceClient(endpoint=STORAGE_ACC_ENDPOINT, credential=credential)

app = Flask(__name__)
cors = CORS(app)


@app.route('/api/totalamount', methods=['POST'])
def entry():
    try:
        print(request.headers)
        request_data = request.get_json()
        print(request_data)
        user_name = request_data['user_name']
        user_id = request_data['user_id']
        no_of_items = int(request_data['no_of_items'])
        amount = int(request_data['amount'])
        tax = 18
        total_amount = round((amount * (tax / 100)) + amount, 2)
        print(user_name, user_id, no_of_items, amount, total_amount)
        my_entity = {
            u'PartitionKey': user_name,
            u'RowKey': user_id,
            u'No_Of_Items': no_of_items,
            u'Amount': amount,
            u'Tax': str(tax) + '%',
            u'Total_Amount': total_amount
        }
        table_client = service.get_table_client(table_name="apitesttable")
        entity = table_client.create_entity(entity=my_entity)
        return jsonify(f"The entity has been added")
    except Exception as e:
        return jsonify(f"something went wrong! check logs - {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)