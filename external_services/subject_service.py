materials = {
    "phys": "https://xn-----glccgu7bzhf.xn--p1ai/materials/physics_formulas.pdf",
    "maths": "http://repet.by/files/math_form.pdf",
    "rus": "http://www.brovkoekaterina.ru/gallery/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9.%20%D0%B2%D1%81%D1%8F%20%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B2%20%D1%81%D1%85%D0%B5%D0%BC%D0%B0%D1%85%20%D0%B8%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%D1%85.pdf",
    "chem": "https://100ballnik.com/wp-content/uploads/2021/08/spravochnik-ege2022-himiya-1.pdf",
    "lit": "https://telegra.ph/Literatura-s-5-11-klass-12-15",
    "it": "https://vopvet.ru/PDF/shpori_inf/Shpargalka_EGE_Informatika_pdf.pdf",
}


def get_material(subject):
    return materials.get(subject)
