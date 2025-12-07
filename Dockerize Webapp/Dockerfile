# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy application code
COPY . .

# Step 6: Expose port
EXPOSE 5000

# Step 7: Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
