def netto(brutto, vat):
    if vat >= 0 and vat <=100:
        return brutto - (brutto * vat * 0.01)
    else:
        return "zla wartosc vat!"