from job_parser import parse_job_posting

with open("job_example.txt", "r", encoding="utf-8") as f:
    job_text = f.read()

parsed = parse_job_posting(job_text)

print("Parsed Job Info")
print(parsed)