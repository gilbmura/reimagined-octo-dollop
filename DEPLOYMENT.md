# Deployment Guide for Render

## Prerequisites

1. **Cloud Database Setup**
   - Choose one: PlanetScale, AWS RDS, Google Cloud SQL, or Railway
   - Create a MySQL database
   - Note down connection details

2. **GitHub Repository**
   - Push your code to GitHub
   - Ensure all files are committed

## Render Deployment Steps

### 1. Connect to Render
1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository

### 2. Configure Service
- **Name**: `urban-mobility-dashboard`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `cd backend && gunicorn app:app --bind 0.0.0.0:$PORT`

### 3. Environment Variables
Set these in Render dashboard:
```
DB_HOST=your_cloud_database_host
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
DB_PORT=3306
```

### 4. Database Setup
Run these commands on your cloud database:
```sql
-- Run schema.sql
source db/schema.sql;

-- Run user initialization
source db/01-init-user-and-db.sql;

-- Load your data using simple_loader.py
python scripts/simple_loader.py --csv-file data/processed/cleaned.csv
```

### 5. Deploy
- Click "Create Web Service"
- Wait for build to complete
- Your app will be available at the provided URL

## Database Options

### PlanetScale (Recommended)
1. Sign up at [planetscale.com](https://planetscale.com)
2. Create new database
3. Get connection string
4. Use connection details in Render environment variables

### Railway Database
1. Sign up at [railway.app](https://railway.app)
2. Create MySQL database
3. Get connection string
4. Use in Render environment variables

### AWS RDS
1. Create RDS MySQL instance
2. Configure security groups
3. Get endpoint and credentials
4. Use in Render environment variables

## Troubleshooting

### Common Issues
1. **Database Connection Failed**
   - Check environment variables
   - Verify database is accessible from Render
   - Check firewall settings

2. **Build Failed**
   - Check requirements.txt
   - Verify Python version compatibility

3. **App Crashes**
   - Check logs in Render dashboard
   - Verify database connection
   - Check environment variables

### Logs
- View logs in Render dashboard
- Check for database connection errors
- Verify all environment variables are set

## Post-Deployment

1. **Test the application**
   - Visit the provided URL
   - Check if dashboard loads
   - Test date filtering

2. **Monitor performance**
   - Check Render metrics
   - Monitor database usage
   - Set up alerts if needed

## Security Notes

- Never commit `.env` files
- Use strong database passwords
- Enable SSL for database connections
- Regularly update dependencies