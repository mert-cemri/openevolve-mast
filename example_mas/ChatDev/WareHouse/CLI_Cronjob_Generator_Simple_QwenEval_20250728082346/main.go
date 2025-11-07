'''
main.go contains the main function to run the application as a CLI or GUI.
It handles command-line arguments and initializes the GUI if no arguments are provided.
'''
package main
import (
	"fmt"
	"os"
	"github.com/fyne-io/fyne/v2/app"
	"github.com/yourusername/chatdev/cronjob"
)
func main() {
	if len(os.Args) > 1 {
		// CLI mode
		schedule := os.Args[1]
		cronJob := cronjob.NewCronJob()
		cronJob.SetSchedule(schedule)
		output := cronJob.Generate()
		fmt.Println(output)
	} else {
		// GUI mode
		a := app.New()
		createGUI(a)
		a.Run()
	}
}
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