def calculate_electricity_bill():
    """Calculate electricity bill based on units consumed"""
    
    print("=" * 60)
    print("ELECTRICITY BILL CALCULATOR")
    print("=" * 60)
    
    try:
        # Get customer details
        customer_name = input("\nEnter Customer Name: ").strip()
        customer_id = input("Enter Customer ID: ").strip()
        
        # Get units consumed
        units = float(input("Enter Units Consumed (kWh): "))
        
        if units < 0:
            print("❌ Units cannot be negative!")
            return
        
        # Tiered pricing structure (common billing rates)
        # Rates per unit in different slabs
        if units <= 100:
            rate = 5.0  # Rs 5 per unit for first 100 units
            charge = units * rate
        elif units <= 200:
            charge = 100 * 5.0  # First 100 units
            charge += (units - 100) * 7.0  # Next 100 units at Rs 7
        elif units <= 300:
            charge = 100 * 5.0  # First 100 units
            charge += 100 * 7.0  # Next 100 units
            charge += (units - 200) * 10.0  # Next 100 units at Rs 10
        else:
            charge = 100 * 5.0  # First 100 units
            charge += 100 * 7.0  # Next 100 units
            charge += 100 * 10.0  # Next 100 units
            charge += (units - 300) * 12.0  # Above 300 units at Rs 12
        
        # Additional charges
        fixed_charge = 50  # Fixed monthly charge
        tax_percent = 10  # 10% tax
        
        # Calculate total
        subtotal = charge + fixed_charge
        tax = (subtotal * tax_percent) / 100
        total_bill = subtotal + tax
        
        # Display bill
        print("\n" + "=" * 60)
        print("ELECTRICITY BILL")
        print("=" * 60)
        print(f"Customer Name: {customer_name}")
        print(f"Customer ID: {customer_id}")
        print("-" * 60)
        print(f"Units Consumed: {units} kWh")
        print("-" * 60)
        print("RATE DETAILS:")
        print(f"  Units (0-100): {min(units, 100):.2f} × Rs 5.00 = Rs {min(units, 100) * 5:.2f}")
        
        if units > 100:
            slab2_units = min(units - 100, 100)
            print(f"  Units (101-200): {slab2_units:.2f} × Rs 7.00 = Rs {slab2_units * 7:.2f}")
        
        if units > 200:
            slab3_units = min(units - 200, 100)
            print(f"  Units (201-300): {slab3_units:.2f} × Rs 10.00 = Rs {slab3_units * 10:.2f}")
        
        if units > 300:
            slab4_units = units - 300
            print(f"  Units (301+): {slab4_units:.2f} × Rs 12.00 = Rs {slab4_units * 12:.2f}")
        
        print("-" * 60)
        print("BILL SUMMARY:")
        print(f"  Energy Charge: Rs {charge:.2f}")
        print(f"  Fixed Monthly Charge: Rs {fixed_charge:.2f}")
        print(f"  Subtotal: Rs {subtotal:.2f}")
        print(f"  Tax ({tax_percent}%): Rs {tax:.2f}")
        print("=" * 60)
        print(f"TOTAL AMOUNT DUE: Rs {total_bill:.2f}")
        print("=" * 60)
        
        # Payment reminder
        print("\n📌 Payment due within 5 days of bill generation.")
        print("Late payment may incur additional charges.")
        print("=" * 60)
    
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    calculate_electricity_bill()
    
    # Option to calculate another bill
    while True:
        choice = input("\nDo you want to calculate another bill? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            print("\n")
            calculate_electricity_bill()
        elif choice in ['no', 'n']:
            print("\nThank you for using Electricity Bill Calculator!")
            break
        else:
            print("Please enter 'yes' or 'no'.")