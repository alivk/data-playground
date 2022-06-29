import pandas as pd

output_filename = './aws-data-conversion/template_table.csv'

# create a DataFrame for output template
delivery_country = ['Indonesia', 'Malaysia', 'Vietnam', 'Singapore', 'Philippines', 'Thailand']
activity_type = ['Class', 'Delivery driven event', 'Marketing influenced event']
activity_audience = ['Commercial Private', 'Commercial Semi-Private', 'Public', 'Internal']
activity_status = ['Active', 'Completed', 'Hold', 'Canceled']
country_audience = [(a, b, c, d) for a in delivery_country 
                                 for b in activity_type 
                                 for c in activity_audience
                                 for d in activity_status]
template_df = pd.DataFrame(country_audience,
                           columns=['delivery_country', 'activity_type', 'activity_audience', 'activity_status'])
template_df.to_csv(output_filename, index_label='No')
