'''
In this implementation, the NotificationService class directly depends on the
EmailSender class, which violates the Dependency Inversion Principle. The high-level
NotificationService should not depend on the low-level EmailSender, as it tightly
couples the classes together.
Redesign this program to follow the Dependency Inversion Principle (DIP) principle
which represents that “Abstractions should not depend upon details. Details
should depend upon abstractions.”

'''
from abc import ABC, abstractmethod

# Abstraction for communication mechanism
class CommunicationSender(ABC):
    @abstractmethod
    def send_message(self, recipient, subject, message):
        pass

# Concrete implementation of CommunicationSender
class EmailSender(CommunicationSender):
    def send_message(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")

# NotificationService depends on CommunicationSender abstraction
class NotificationService:
    def __init__(self, communication_sender):
        self.communication_sender = communication_sender

    def send_notification(self, recipient, message):
        self.communication_sender.send_message(recipient, "Notification", message)

# Using the NotificationService with EmailSender
email_sender = EmailSender()
notification_service = NotificationService(email_sender)
notification_service.send_notification("user@example.com", "Hello, this is a notification!")
