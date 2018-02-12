import time
import notify2



notifications = [
	"First Notif"
]

notify2.init("AI Notifications")

notice = notify2.Notification(None)
notice.set_urgency(notify2.URGENCY_NORMAL)
notice.set_timeout(10000)


for notification in notifications:
	notice.update("Notifs" , notification)
	notice.show()
	n = notify2.Notification("Notifs",icon=ICON,message=notification)
	notice.set_urgency(notify2.URGENCY_NORMAL)
	notice.set_timeout(6000)
	n.show()
	time.sleep(7)
