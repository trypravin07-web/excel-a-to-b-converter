from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_excel(file)

        df_b = pd.DataFrame({
            "store_id": df["store_identifier"],
            "sku_id": df["lookup_code"],
            "name": df["item_name"],
            "size": df["size"],
            "description": df["size_uom"],        # ✅ FINAL FIX
            "cost_unit": df["cost_unit"],
            "price": df["price"],
            "department": df["department"],
            "aisle": df["aisle"],
            "is_active": "",
            "is_alcohol": "",
            "is_weighted_item": "",
            "image_URL": df["remote_image_URL"]
        })

        output = "B_converted.xlsx"
        df_b.to_excel(output, index=False)

        return send_file(output, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
