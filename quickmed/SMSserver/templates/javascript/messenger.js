exports.handler = function(context, event, callback) {
	// Fetch already initialized Twilio REST client
	const twilioClient = context.getTwilioClient();

	twilioClient.messages.create({
		from: from,
		to: to,
		body: 'create using callback'
	}, function(err, result) {
		console.log('Created message using callback');
		console.log(result.sid);
		callback();
	});
}
