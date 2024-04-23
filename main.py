import csv

def read_product_info(csv_file):
    product_info = {'Name': [], 'Price': [], 'Rating': []}
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_info['Name'].append(row.get('Name', ''))
                product_info['Price'].append(row.get('Price', ''))
                product_info['Rating'].append(row.get('Rating', ''))
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return product_info

def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraped Product Information</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>

    <h2>Scraped Product Information</h2>

    <table id="productTable">
        <thead>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Rating</th>
            </tr>
        </thead>
        <tbody>
    """

    for i in range(len(data['Price'])):
        html_content += f"""
            <tr>
                <td>{data['Name'][i]}</td>
                <td>{data['Price'][i]}</td>
                <td>{data['Rating'][i]}</td>
            </tr>
        """

    html_content += """
        </tbody>
    </table>

    </body>
    </html>
    """

    with open('scraped_products.html', 'w', encoding='utf-8') as file:
        file.write(html_content)


if __name__ == "__main__":
    csv_file = 'products.csv'
    product_info = read_product_info(csv_file)
    print(product_info)
    generate_html(product_info)
    print("HTML file generated successfully!")
