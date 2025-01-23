<?php
// Replace 'YOUR_BOT_API_TOKEN' with the token from BotFather
$botToken = "YOUR_BOT_API_TOKEN";
$apiUrl = "https://api.telegram.org/bot$botToken/";

// Get incoming updates from Telegram
$update = file_get_contents("php://input");
$update = json_decode($update, TRUE);

// Check if a message was sent
if (isset($update["message"])) {
    $chatId = $update["message"]["chat"]["id"]; // Chat ID to send responses
    $messageText = $update["message"]["text"]; // The text of the user's message

    // Define a simple response
    $responseText = "Hello! You sent: " . $messageText;

    // Handle a specific command (e.g., /start)
    if ($messageText === "/start") {
        $responseText = "Welcome to my bot! Type anything to get a response.";
    }

    // Send a message back to the user
    $sendMessageUrl = $apiUrl . "sendMessage?chat_id=$chatId&text=" . urlencode($responseText);
    file_get_contents($sendMessageUrl);
}
?>
