from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_excel(file)

        def col(name):
            return df[name] if name in df.columns else ""

        df_b = pd.DataFrame({
            "store_id": col("store_identifier"),
            "sku_id": col("lookup_code"),
            "name": col("item_name"),
            "size": col("size"),
            "description": col("size_uom"),
            "cost_unit": col("cost_unit"),
            "price": col("price"),
            "department": col("department"),
            "aisle": col("aisle"),
            "is_active": "",
            "is_alcohol": "",
            "is_weighted_item": "",
            "image_URL": col("remote_image_URL")
        })

        output = "DoorDash_Formatted.xlsx"
        df_b.to_excel(output, index=False)
        return send_file(output, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
