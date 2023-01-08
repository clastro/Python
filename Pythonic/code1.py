p_hat = late_shipments[late_shipments['late'] == "Yes"].mean()
p_hat = (late_shipments['late'] == "Yes").mean()
