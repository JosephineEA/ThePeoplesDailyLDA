function [documents] = preprocessRMRB(textData)

% Convert the text data to lowercase.
cleanTextData = lower(textData);

% Tokenize the text.
documents = tokenizedDocument(cleanTextData);

% Erase punctuation.
documents = erasePunctuation(documents);

% Remove a list of stop words.
documents = removeStopWords(documents);

% Remove words with 2 or fewer characters,
% and words with 15 or greater characters.
documents = removeShortWords(documents,1);
documents = removeLongWords(documents,15);

% Lemmatize the words.
documents = addPartOfSpeechDetails(documents);  % No definition
documents = normalizeWords(documents,'Style','lemma'); 

end
