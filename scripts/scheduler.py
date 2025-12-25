"""Pipeline scheduler for Phase 5"""
import schedule
import time
import logging
from pipeline_orchestrator import PipelineOrchestrator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PipelineScheduler:
    def __init__(self):
        self.orchestrator = PipelineOrchestrator()
        self.is_running = False
    
    def schedule_daily_pipeline(self):
        """Schedule pipeline to run daily at 2 AM"""
        schedule.every().day.at('02:00').do(self.run_pipeline)
        logger.info('Scheduled daily pipeline at 02:00')
    
    def schedule_hourly_pipeline(self):
        """Schedule pipeline to run every hour"""
        schedule.every().hour.do(self.run_pipeline)
        logger.info('Scheduled hourly pipeline')
    
    def run_pipeline(self):
        """Run the pipeline"""
        logger.info('Running scheduled pipeline...')
        return self.orchestrator.run_pipeline()
    
    def start_scheduler(self):
        """Start the scheduler loop"""
        self.is_running = True
        logger.info('Scheduler started')
        
        while self.is_running:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                logger.info('Scheduler interrupted')
                self.stop_scheduler()
            except Exception as e:
                logger.error(f'Scheduler error: {str(e)}')
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.is_running = False
        logger.info('Scheduler stopped')

if __name__ == '__main__':
    scheduler = PipelineScheduler()
    scheduler.schedule_daily_pipeline()
    scheduler.start_scheduler()
