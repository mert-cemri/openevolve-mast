'''
This file contains the CronJob struct and its methods to generate cron job schedules.
'''
package cronjob
import (
	"fmt"
)
// CronJob represents a cron job with a specific schedule.
type CronJob struct {
	schedule string
}
// NewCronJob creates a new CronJob instance.
func NewCronJob() *CronJob {
	return &CronJob{}
}
// SetSchedule sets the schedule for the cron job.
func (c *CronJob) SetSchedule(schedule string) {
	c.schedule = schedule
}
// Generate generates the cron job line based on the schedule.
func (c *CronJob) Generate() string {
	switch c.schedule {
	case "daily at 3 AM":
		return "0 3 * * *"
	case "every 15 minutes":
		return "*/15 * * * *"
	case "weekly on Monday at 4 AM":
		return "0 4 * * 1"
	case "monthly on the 1st at 5 AM":
		return "0 5 1 * *"
	case "hourly":
		return "0 * * * *"
	case "every 5 minutes":
		return "*/5 * * * *"
	case "every 30 minutes":
		return "*/30 * * * *"
	case "daily at midnight":
		return "0 0 * * *"
	case "daily at noon":
		return "0 12 * * *"
	default:
		return "Invalid schedule. Please use one of the following: daily at 3 AM, every 15 minutes, weekly on Monday at 4 AM, monthly on the 1st at 5 AM, hourly, every 5 minutes, every 30 minutes, daily at midnight, daily at noon"
	}
}