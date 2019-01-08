import sys
import flask
import pytext
config_file = sys.argv[1]
model_file = sys.argv[2]

config = pytext.load_config(config_file)
predictor = pytext.create_predictor(config, model_file)
text = input('\nPlease Enter the text\n')
result = predictor({"raw_text": text})
doc_label_scores_prefix = (
        'scores:' if any(r.startswith('scores:') for r in result)
        else 'doc_scores:'
    )

    # For now let's just output the top document label!
best_doc_label = max(
        (label for label in result if label.startswith(doc_label_scores_prefix)),
        key=lambda label: result[label][0],
    # Strip the doc label prefix here
    )[len(doc_label_scores_prefix):]
print(best_doc_label)