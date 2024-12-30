def calculate_crypto_tax(buy_price, sell_price, quantity, fees, tax_rate):
    gain_loss = (sell_price - buy_price) * quantity - fees
    tax = max(0, gain_loss * tax_rate / 100)
    return gain_loss, tax
