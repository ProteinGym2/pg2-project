#!/bin/sh

printf "current dir is"
pwd

if [ "{{ cookiecutter.data_sources }}" != "#*" ]; then
	for url in {{ cookiecutter.data_sources }}; do
		if [ $url = "http"* ]; then
			echo "download contents of $url"
		else
			VERSION="v1.2"
			curl -o ${url} https://marks.hms.harvard.edu/proteingym/ProteinGym_${VERSION}/${url}
			unzip ${url} && rm ${url}
		fi
	done
fi
