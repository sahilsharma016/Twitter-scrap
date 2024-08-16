input_file_path = 'links.txt'
output_file_path = 'dropped_duplicates.txt'

unique_urls = set()

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

for line in lines:
    url = line.strip()
    if url not in unique_urls:
        unique_urls.add(url)

# Write unique URLs to a new file
with open(output_file_path, 'w') as output_file:
    for url in unique_urls:
        output_file.write(url + '\n')

print(f'Duplicates dropped. Unique URLs saved to {output_file_path}')

