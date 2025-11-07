'''
gui.go contains the GUI components and logic for the application.
It creates the GUI window, handles user input, and updates the output label with the generated cron job.
'''
package main
import (
	"github.com/fyne-io/fyne/v2"
	"github.com/fyne-io/fyne/v2/app"
	"github.com/fyne-io/fyne/v2/container"
	"github.com/fyne-io/fyne/v2/widget"
	"github.com/yourusername/chatdev/cronjob"
)
// createGUI creates the GUI window.
func createGUI(a fyne.App) {
	window := a.NewWindow("Cronjob Generator")
	scheduleEntry := widget.NewEntry()
	scheduleEntry.SetPlaceHolder("Enter schedule (e.g., daily at 3 AM, every 15 minutes)")
	outputLabel := widget.NewLabel("")
	generateButton := widget.NewButton("Generate", func() {
		handleGenerate(scheduleEntry.Text, outputLabel)
	})
	window.SetContent(container.NewVBox(
		scheduleEntry,
		generateButton,
		outputLabel,
	))
	window.Show()
}
// handleGenerate handles the generate button click event.
func handleGenerate(schedule string, outputLabel *widget.Label) {
	cronJob := cronjob.NewCronJob()
	cronJob.SetSchedule(schedule)
	output := cronJob.Generate()
	if output == "Invalid schedule. Please use one of the following: daily at 3 AM, every 15 minutes, weekly on Monday at 4 AM, monthly on the 1st at 5 AM, hourly, every 5 minutes, every 30 minutes, daily at midnight, daily at noon" {
		outputLabel.SetText(output)
	} else {
		outputLabel.SetText(output) // Update the GUI label with the output
	}
}